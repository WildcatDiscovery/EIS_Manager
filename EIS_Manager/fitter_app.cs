using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Diagnostics;
using System.IO;
using System.Windows.Forms.DataVisualization.Charting;
using System.Text.RegularExpressions;

namespace EIS_Manager
{
   

    public partial class Fitter : Form
    {
        public List<Double> freq = new List<double>();
        public List<Double> re = new List<double>();
        public List<Double> im = new List<double>();
        public List<Double> fit_re = new List<double>();
        public List<Double> fit_im = new List<double>();
        public bool fitted = new bool();
        public string python_script_location;
        public string[] pre_test;
        public string[] post_test;
        public string temp;
        public List<string> to_export = new List<string>();
        public string curr_path;
        public int bad_index = new int();
        public List<String> lst_fits = new List<String>();
        public List<Double> hold_freq = new List<double>();
        public List<Double> hold_re = new List<double>();
        public List<Double> hold_im = new List<double>();
        public bool recalibrated = new bool();
        List<int> bad_ints = new List<int>();
        List<int> recal_ints = new List<int>();

        public class mpt
        {
            public string Name
            { get; set; }

            public string Mask_choice
            { get; set; }

            public bool Recal
            { get; set; }

            public double X_min
            { get; set; }

            public double X_max
            { get; set; }

            public double Y_min
            { get; set; }

            public double Y_max
            { get; set; }

            public List<int> bad_indices = new List<int>();

            public Dictionary<Double, Tuple<Double, Double>> mpt_dict = new Dictionary<Double, Tuple<Double, Double>>();

            public int recal_setting = 0;
        }

        public mpt curr_mpt = new mpt();

        //Development version will be using either a class or dictionary or both
        public List<mpt> saved_files = new List<mpt>();
        
        public Fitter()
        {
            InitializeComponent();
            nvyquist.ChartAreas[0].CursorX.IsUserSelectionEnabled = true;
            nvyquist.ChartAreas[0].CursorX.IsUserEnabled = true;
            nvyquist.ChartAreas[0].CursorX.LineColor = Color.Transparent;
            nvyquist.ChartAreas[0].CursorX.SelectionColor = Color.Lime;
            nvyquist.ChartAreas[0].CursorX.Interval = 0;
            nvyquist.ChartAreas[0].AxisX.ScaleView.Zoomable = true;
            nvyquist.ChartAreas[0].AxisX2.ScaleView.Zoomable = true;

            nvyquist.ChartAreas[0].CursorY.IsUserSelectionEnabled = true;
            nvyquist.ChartAreas[0].CursorY.IsUserEnabled = true;
            nvyquist.ChartAreas[0].CursorY.LineColor = Color.Transparent;
            nvyquist.ChartAreas[0].CursorY.SelectionColor = Color.Lime;
            nvyquist.ChartAreas[0].CursorY.Interval = 0;
            nvyquist.ChartAreas[0].AxisY.ScaleView.Zoomable = true;
            nvyquist.ChartAreas[0].AxisY2.ScaleView.Zoomable = true;



            first_twenty.ChartAreas[0].CursorX.IsUserSelectionEnabled = true;
            first_twenty.ChartAreas[0].CursorX.IsUserEnabled = true;
            first_twenty.ChartAreas[0].CursorX.LineColor = Color.Transparent;
            first_twenty.ChartAreas[0].CursorX.SelectionColor = Color.Lime;
            first_twenty.ChartAreas[0].CursorX.Interval = 0;
            first_twenty.ChartAreas[0].AxisX.ScaleView.Zoomable = true;
            first_twenty.ChartAreas[0].AxisX2.ScaleView.Zoomable = true;

            first_twenty.ChartAreas[0].CursorY.IsUserSelectionEnabled = true;
            first_twenty.ChartAreas[0].CursorY.IsUserEnabled = true;
            first_twenty.ChartAreas[0].CursorY.LineColor = Color.Transparent;
            first_twenty.ChartAreas[0].CursorY.SelectionColor = Color.Lime;
            first_twenty.ChartAreas[0].CursorY.Interval = 0;
            first_twenty.ChartAreas[0].AxisY.ScaleView.Zoomable = true;
            first_twenty.ChartAreas[0].AxisY2.ScaleView.Zoomable = true;

            python_script_location = "C:\\Users\\cjang.WILDCAT\\Desktop\\EIS_Manager\\utils";
            to_export.Add("index, file, fit_R, fit_Rs, fit_n, fit_Q, fit_R2, fit_n2, fit_Q2, fit_n3, fit_Q3");
        }
        
        private void python_scripts_Click(object sender, EventArgs e)
        {
            MessageBox.Show(python_script_location);
            if (folderBrowserDialog2.ShowDialog() == DialogResult.OK)
            {
                python_script_location = folderBrowserDialog2.SelectedPath.ToString();
                MessageBox.Show(python_script_location);
            }
        }

        private string[] path_listing(string path)
        {
            
            string pt1 = python_script_location;
            string progToRun = pt1 + "\\path_listing.py";
            char[] splitter = { '\r' };

            Process proc = new Process();
            proc.StartInfo.FileName = "python.exe";
            proc.StartInfo.RedirectStandardOutput = true;
            proc.StartInfo.UseShellExecute = false;
            proc.StartInfo.Arguments = string.Concat(progToRun, " ", path.ToString());
            proc.Start();

            StreamReader sReader = proc.StandardOutput;
            string[] output = sReader.ReadToEnd().Split(splitter);
            return output;
        }

        private string[] mpt_dataframe(string raw_path, string mpt_file)
        {
            Process proc = new Process();
            proc.StartInfo.FileName = "python.exe";
            proc.StartInfo.RedirectStandardOutput = true;
            proc.StartInfo.UseShellExecute = false;
            string pt1 = python_script_location;
            string progToRun = pt1 + "\\mpt_dataframe.py";
            char[] splitter = { '\r' };
            //"from tools import *; print(mpt_data(path=r'C:\Users\cjang\Desktop\Kyler_Speed_Circuit\data\\',data = ['DE_49_8_30.mpt']).guess_and_plot(mask = [1000018.6, 28]))"
            proc.StartInfo.Arguments = progToRun + " " + raw_path + " " + mpt_file;
            proc.Start();

            StreamReader sReader = proc.StandardOutput;
            string[] output = sReader.ReadToEnd().Split(splitter);

            return output;
        }

        private string[] guesser(string raw_path, string mpt_file)
        {
            //Console.WriteLine(raw_path);
            //Console.WriteLine(mpt_file);
            string pt1 = python_script_location;
            string progToRun = pt1 + "\\guesser.py";
            char[] splitter = { '\r' };

            Process proc = new Process();
            proc.StartInfo.FileName = "python.exe";
            proc.StartInfo.RedirectStandardOutput = true;
            proc.StartInfo.UseShellExecute = false;
            proc.StartInfo.Arguments = progToRun + " " + raw_path + " " + mpt_file;
            proc.Start();
            //MessageBox.Show("Python is Processing; Error Box will fill when process is finished");
            StreamReader sReader = proc.StandardOutput;
            string[] output = sReader.ReadToEnd().Split(splitter);
            //Console.WriteLine(output.Length);
            return output;
        }

        

        private string[] masker(string path, string mpt_file, string mask_choice)
        {
            string pt1 = python_script_location;
            string progToRun = pt1 + "\\masker.py";
            char[] splitter = { '\r' };

            Process proc = new Process();
            proc.StartInfo.FileName = "python.exe";
            proc.StartInfo.RedirectStandardOutput = true;
            proc.StartInfo.UseShellExecute = false;
            proc.StartInfo.Arguments = string.Concat(progToRun, " ", path, " ", mpt_file, " ", mask_choice);
            proc.Start();

            StreamReader sReader = proc.StandardOutput;
            string[] output = sReader.ReadToEnd().Split(splitter);

            return output;
        }

        private string[] masked_mpt(string path, string mpt_file, string mask_choice)
        {
            string pt1 = python_script_location;
            string progToRun = pt1 + "\\masked_df.py";
            char[] splitter = { '\r' };

            Process proc = new Process();
            proc.StartInfo.FileName = "python.exe";
            proc.StartInfo.RedirectStandardOutput = true;
            proc.StartInfo.UseShellExecute = false;
            proc.StartInfo.Arguments = string.Concat(progToRun, " ", path, " ", mpt_file, " ", mask_choice);
            proc.Start();

            StreamReader sReader = proc.StandardOutput;
            string[] output = sReader.ReadToEnd().Split(splitter);

            return output;
        }

        private string[] masked_guesser(string path, string mpt_file, string mask_choice)
        {
            string pt1 = python_script_location;
            string progToRun = pt1 + "\\masked_guesser.py";
            char[] splitter = { '\r' };

            Process proc = new Process();
            proc.StartInfo.FileName = "python.exe";
            proc.StartInfo.RedirectStandardOutput = true;
            proc.StartInfo.UseShellExecute = false;
            proc.StartInfo.Arguments = string.Concat(progToRun, " ", path, " ", mpt_file, " ", mask_choice);
            proc.Start();

            StreamReader sReader = proc.StandardOutput;
            string[] output = sReader.ReadToEnd().Split(splitter);

            return output;
        }

        private string[] window_mask(string path, string mpt_file, string x_min, string x_max, string y_min, string y_max)
        {
            string pt1 = python_script_location;
            string progToRun = pt1 + "\\window_masker.py";
            char[] splitter = { '\r' };

            Process proc = new Process();
            proc.StartInfo.FileName = "python.exe";
            proc.StartInfo.RedirectStandardOutput = true;
            proc.StartInfo.UseShellExecute = false;
            proc.StartInfo.Arguments = string.Concat(progToRun, " ", path, " ", mpt_file, " ", x_min, " ", x_max, " ", y_min, " ", y_max);
            proc.Start();

            StreamReader sReader = proc.StandardOutput;
            string[] output = sReader.ReadToEnd().Split(splitter);

            return output;
        }

        private string[] window_mpt(string path, string mpt_file, string x_min, string x_max, string y_min, string y_max)
        {
            string pt1 = python_script_location;
            string progToRun = pt1 + "\\window_df.py";
            char[] splitter = { '\r' };

            Process proc = new Process();
            proc.StartInfo.FileName = "python.exe";
            proc.StartInfo.RedirectStandardOutput = true;
            proc.StartInfo.UseShellExecute = false;
            proc.StartInfo.Arguments = string.Concat(progToRun, " ", path, " ", mpt_file, " ", x_min, " ", x_max, " ", y_min, " ", y_max);
            proc.Start();

            StreamReader sReader = proc.StandardOutput;
            string[] output = sReader.ReadToEnd().Split(splitter);

            return output;
        }

        private string[] window_masked_fit(string path, string mpt_file, string x_min, string x_max, string y_min, string y_max)
        {
            string pt1 = python_script_location;
            string progToRun = pt1 + "\\window_guesser.py";
            char[] splitter = { '\r' };

            Process proc = new Process();
            proc.StartInfo.FileName = "python.exe";
            proc.StartInfo.RedirectStandardOutput = true;
            proc.StartInfo.UseShellExecute = false;
            //MessageBox.Show(string.Concat(progToRun, " ", path, " ", mpt_file, " ", x_min, " ", x_max, " ", y_min, " ", y_max));
            //Console.WriteLine(string.Concat(progToRun, " ", path, " ", mpt_file, " ", x_min, " ", x_max, " ", y_min, " ", y_max));
            proc.StartInfo.Arguments = string.Concat(progToRun, " ", path, " ", mpt_file, " ", x_min, " ", x_max, " ", y_min, " ", y_max);
            proc.Start();

            StreamReader sReader = proc.StandardOutput;
            string[] output = sReader.ReadToEnd().Split(splitter);

            return output;
        }

        private string[] recal_guesser(string path, string mpt_file, string mask_choice, string indices)
        {
            string pt1 = python_script_location;
            string progToRun = pt1 + "\\recal_guesser.py";
            char[] splitter = { '\r' };
            Process proc = new Process();
            proc.StartInfo.FileName = "python.exe";
            proc.StartInfo.RedirectStandardOutput = true;
            proc.StartInfo.UseShellExecute = false;
            //MessageBox.Show(string.Concat(progToRun, " ", path, " ", mpt_file, " ", mask_choice, " ", indices));
            proc.StartInfo.Arguments = string.Concat(progToRun, " ", path, " ", mpt_file, " ", mask_choice, " ", indices);
            proc.Start();

            StreamReader sReader = proc.StandardOutput;
            string[] output = sReader.ReadToEnd().Split(splitter);

            return output;
        }

        private string[] recal_window_guesser(string path, string mpt_file, string x_min, string x_max, string y_min, string y_max, string indices)
        {
            string pt1 = python_script_location;
            string progToRun = pt1 + "\\recal_window_guesser.py";
            char[] splitter = { '\r' };

            Process proc = new Process();
            proc.StartInfo.FileName = "python.exe";
            proc.StartInfo.RedirectStandardOutput = true;
            proc.StartInfo.UseShellExecute = false;
            //MessageBox.Show(string.Concat(progToRun, " ", path, " ", mpt_file, " ", x_min, " ", x_max, " ", y_min, " ", y_max, " ", indices));
            //Console.WriteLine(string.Concat(progToRun, " ", path, " ", mpt_file, " ", x_min, " ", x_max, " ", y_min, " ", y_max, " ", indices));
            proc.StartInfo.Arguments = string.Concat(progToRun, " ", path, " ", mpt_file, " ", x_min, " ", x_max, " ", y_min, " ", y_max, " ", indices);
            proc.Start();

            StreamReader sReader = proc.StandardOutput;
            string[] output = sReader.ReadToEnd().Split(splitter);

            return output;
        }

        private void btnFit_Click(object sender, EventArgs e)
        {
        }

        private void button2_Click(object sender, EventArgs e)
        {
        }

        private void lin_kk_mask_CheckedChanged(object sender, EventArgs e)
        {
        }

        private void textBox4_TextChanged(object sender, EventArgs e)
        {
        }

        private void Fitter_Load(object sender, EventArgs e)
        {
        }

        private void pathbutton_Click_1(object sender, EventArgs e)
        {
            if (folderBrowserDialog1.ShowDialog() == DialogResult.OK)
            {
                curr_path = folderBrowserDialog1.SelectedPath.ToString();
                Debug.WriteLine(curr_path);
                file_display.Items.Clear();
                
                string box_form = string.Join(", ", path_listing(folderBrowserDialog1.SelectedPath));
                if (box_form.Length > 0)
                {

                    path_list_box.Text = box_form;

                    foreach (string single_file in path_listing(folderBrowserDialog1.SelectedPath))
                    {
                        file_display.Items.Add(single_file);
                    }
                }
                else
                {
                    MessageBox.Show("Empty folder or a bad directory");
                }
                pre_test = path_list_box.Text.Split(' ');
                post_test = new string[pre_test.Length];
                
            }
        }

        private void nvyquist_mousewheel(object sender, MouseEventArgs e)
        {
            var chart = (Chart)sender;
            var xAxis = chart.ChartAreas[0].AxisX;
            var yAxis = chart.ChartAreas[0].AxisY;

            try
            {
                var xMin = xAxis.ScaleView.ViewMinimum;
                var xMax = xAxis.ScaleView.ViewMaximum;
                var yMin = yAxis.ScaleView.ViewMinimum;
                var yMax = yAxis.ScaleView.ViewMaximum;
                
                if (e.Delta < 0) // Scrolled down.
                {
                    xAxis.ScaleView.ZoomReset();
                    yAxis.ScaleView.ZoomReset();
                    
                }
                else if (e.Delta > 0) // Scrolled up.
                {
                    
                    var posXStart = xAxis.PixelPositionToValue(e.Location.X) - (xMax - xMin) / 8;
                    var posXFinish = xAxis.PixelPositionToValue(e.Location.X) + (xMax - xMin) / 8;
                    var posYStart = yAxis.PixelPositionToValue(e.Location.Y) - (yMax - yMin) / 8;
                    var posYFinish = yAxis.PixelPositionToValue(e.Location.Y) + (yMax - yMin) / 8;

                    xAxis.ScaleView.Zoom(posXStart, posXFinish);
                    yAxis.ScaleView.Zoom(posYStart, posYFinish);
                  
                }
                
            }
            catch { }

        }

        private void file_display_SelectedIndexChanged(object sender, EventArgs e)
        {
            recalibrated = false;
            freq.Clear();
            re.Clear();
            im.Clear();
            fit_re.Clear();
            fit_im.Clear();
            fit_coeffs_box.Clear();
            df_checkbox.Items.Clear();
            bad_ints.Clear();
            no_of_pts.Clear();
            curr_mpt = new mpt();


            foreach (var series in nvyquist.Series)
            {
                series.Points.Clear();
            }
            foreach (var series in first_twenty.Series)
            {
                series.Points.Clear();
            }
            try
            {
                if (string.Join("", post_test).Length > 0)
                {
                    path_list_box.Text = string.Join("", post_test);
                }


                string mpt_file = Regex.Replace(file_display.SelectedItem.ToString(), @"\t|\n|\r", "");
                curr_mpt.Name = mpt_file;

                string raw_path = curr_path;
                file_display_label.Text = mpt_file;
                string[] output = mpt_dataframe(raw_path, file_display.SelectedItem.ToString());
                

                List<string> pre = output.ToList();
                pre.RemoveAt(0);
                string box_form = string.Join("", pre);
               

                foreach (string sgl in pre)
                {
                    Queue<Double> dbl_prep = new Queue<double>();
                    foreach (var word in sgl.Split(' '))
                    {
                        if (word.Length > 5)
                        {
                            dbl_prep.Enqueue(Convert.ToDouble(word));
                        }
                    }
                    if (dbl_prep.Count == 3)
                    {
          
                        curr_mpt.mpt_dict.Add(dbl_prep.Dequeue(), new Tuple<double, double>(dbl_prep.Dequeue(), dbl_prep.Dequeue()));
                    }
                    else
                    {
                        foreach (var word in dbl_prep)
                        {
                            MessageBox.Show("VALUE: " + word.ToString());
                        }
                    }
                }
                
                nvyquist.MouseWheel += nvyquist_mousewheel;
                first_twenty.MouseWheel += nvyquist_mousewheel;
                
                for (int i = 0; i < curr_mpt.mpt_dict.Count; i++)
                {
                    string marker = String.Concat(curr_mpt.mpt_dict.Values.ElementAt(i).Item1.ToString(), " , ", curr_mpt.mpt_dict.Values.ElementAt(i).Item2.ToString());
                    df_checkbox.Items.Add(marker);
                    df_checkbox.SetItemChecked(i, true);
                }
               
                for (int i = 0; i < curr_mpt.mpt_dict.Count; i++)
                {
                    DataPoint point = new DataPoint();
                    point.SetValueXY(curr_mpt.mpt_dict.Values.ElementAt(i).Item1, curr_mpt.mpt_dict.Values.ElementAt(i).Item2);
                    point.ToolTip = string.Format("X Value: {0}, Y Value {1}", curr_mpt.mpt_dict.Values.ElementAt(i).Item1, curr_mpt.mpt_dict.Values.ElementAt(i).Item2);
                    nvyquist.Series[0].Points.Add(point);
                }

                for (int i = 0; i < 20; i++)
                {
                    DataPoint point = new DataPoint();
                    point.SetValueXY(curr_mpt.mpt_dict.Values.ElementAt(i).Item1, curr_mpt.mpt_dict.Values.ElementAt(i).Item2);
                    point.ToolTip = string.Format("X Value: {0}, Y Value {1}", curr_mpt.mpt_dict.Values.ElementAt(i).Item1, curr_mpt.mpt_dict.Values.ElementAt(i).Item2);
                    first_twenty.Series[0].Points.Add(point);
                }

                nvyquist.Series[0].ToolTip = "X Value: #VALX, Y Value: #VALY";
                nvyquist.Series[1].ToolTip = "FITTED X Value: #VALX, FITTED Y Value: #VALY";
                nvyquist.Series[2].ToolTip = "X Value: #VALX, Y Value: #VALY";

                first_twenty.Series[0].ToolTip = "X Value: #VALX, Y Value: #VALY";
                first_twenty.Series[1].ToolTip = "FITTED X Value: #VALX, FITTED Y Value: #VALY";
               
                x_min.Text = Math.Round(nvyquist.ChartAreas[0].AxisX.Minimum, 2).ToString();
                x_max.Text = Math.Round(nvyquist.ChartAreas[0].AxisX.Maximum, 2).ToString();
                y_min.Text = Math.Round(nvyquist.ChartAreas[0].AxisY.Minimum, 2).ToString();
                y_max.Text = Math.Round(nvyquist.ChartAreas[0].AxisY.Maximum, 2).ToString();

            }
            catch (NullReferenceException nullspot)
            {
                MessageBox.Show("Select a Value");
            }

        }


        private void recal_button_Click(object sender, EventArgs e)
        {
            recalibrated = true;
            int count = df_checkbox.Items.Count;
            bad_ints.Clear();
            if (df_checkbox.Items.Count == df_checkbox.CheckedItems.Count)
            {
                recalibrated = false;
            }
            
            for (int index = count; index > 0; index--)
            {
               if (!df_checkbox.CheckedItems.Contains(df_checkbox.Items[index - 1]))
                {
                    if (!bad_ints.Contains(index - 1))
                    {
                        recal_ints.Add((index - 1));
                        bad_ints.Add((index - 1));
                        //df_checkbox.Items.RemoveAt(index - 1);
                    }
                }
            }
            nvyquist.Series[0].Points.Clear();
            for (int i = 0; i < df_checkbox.Items.Count; i++)
            {
                if (df_checkbox.GetItemCheckState(i) == CheckState.Checked)
                {
                    nvyquist.Series[0].Points.AddXY(curr_mpt.mpt_dict.Values.ElementAt(i).Item1, curr_mpt.mpt_dict.Values.ElementAt(i).Item2);
                }
                
            }
            first_twenty.Series[0].Points.Clear();
            for (int i = 0; i < 20; i++)
            {
                if (df_checkbox.GetItemCheckState(i) == CheckState.Checked)
                {
                    first_twenty.Series[0].Points.AddXY(curr_mpt.mpt_dict.Values.ElementAt(i).Item1, curr_mpt.mpt_dict.Values.ElementAt(i).Item2);
                }
            }
            //MessageBox.Show("RECALIBRATED");
            recal_ints.Clear();
        }


        private void masker1_CheckedChanged(object sender, EventArgs e)
        {
            try
            {
                string mpt_file = file_display.SelectedItem.ToString();
                string raw_path = curr_path;
                string[] mask_mpt = masked_mpt(raw_path, mpt_file, "1");

                curr_mpt.Mask_choice = "1";

                List<Double> masked_freq = new List<Double>();
                List<Double> masked_re = new List<Double>();
                List<Double> masked_im = new List<Double>();



                List<string> pre = mask_mpt.ToList();
                pre.RemoveAt(0);
                string box_form = string.Join("", pre);


                foreach (string sgl in pre)
                {
                    Queue<Double> dbl_prep = new Queue<double>();
                    //MessageBox.Show("NEW LINE");
                    foreach (var word in sgl.Split(' '))
                    {
                        if (word.Length > 5)
                        {
                            //MessageBox.Show(word);
                            dbl_prep.Enqueue(Convert.ToDouble(word));
                        }
                    }
                    if (dbl_prep.Count == 3)
                    {
                        masked_freq.Add(dbl_prep.Dequeue());
                        masked_re.Add(dbl_prep.Dequeue());
                        masked_im.Add(dbl_prep.Dequeue());
                    }
                    else
                    {
                        foreach (var word in dbl_prep)
                        {
                            MessageBox.Show("VALUE: " + word.ToString());
                        }
                    }
                }
                //MessageBox.Show(masked_freq.ToList().ToString());
                nvyquist.Series[2].Points.DataBindXY(masked_re, masked_im);
            }
            catch (NullReferenceException)
            {
                MessageBox.Show("Bad path or Bad MPT file; Please Select a folder and a file");
            }
        }

        private void masker2_CheckedChanged(object sender, EventArgs e)
        {
            try
            {
                string mpt_file = file_display.SelectedItem.ToString();
                string raw_path = curr_path;
                string[] mask_mpt = masked_mpt(raw_path, mpt_file, "2");

                curr_mpt.Mask_choice = "2";

                List<Double> masked_freq = new List<Double>();
                List<Double> masked_re = new List<Double>();
                List<Double> masked_im = new List<Double>();



                List<string> pre = mask_mpt.ToList();
                pre.RemoveAt(0);
                string box_form = string.Join("", pre);


                foreach (string sgl in pre)
                {
                    Queue<Double> dbl_prep = new Queue<double>();
                    //MessageBox.Show("NEW LINE");
                    foreach (var word in sgl.Split(' '))
                    {
                        if (word.Length > 5)
                        {
                            dbl_prep.Enqueue(Convert.ToDouble(word));
                        }
                    }
                    if (dbl_prep.Count == 3)
                    {
                        masked_freq.Add(dbl_prep.Dequeue());
                        masked_re.Add(dbl_prep.Dequeue());
                        masked_im.Add(dbl_prep.Dequeue());
                    }
                    else
                    {
                        foreach (var word in dbl_prep)
                        {
                            MessageBox.Show("VALUE: " + word.ToString());
                        }
                    }
                }
                //MessageBox.Show(masked_freq.ToList().ToString());
                nvyquist.Series[2].Points.DataBindXY(masked_re, masked_im);
            }
            catch (NullReferenceException)
            {
                MessageBox.Show("Bad path or Bad MPT file; Please Select a folder and a file");
            }
        }

        private void masker3_CheckedChanged(object sender, EventArgs e)
        {
            
            try
            {
                string mpt_file = file_display.SelectedItem.ToString();
                string raw_path = curr_path;
                string[] mask_mpt = masked_mpt(raw_path, mpt_file, "3");

                curr_mpt.Mask_choice = "3";

                List<Double> masked_freq = new List<Double>();
                List<Double> masked_re = new List<Double>();
                List<Double> masked_im = new List<Double>();



                List<string> pre = mask_mpt.ToList();
                pre.RemoveAt(0);
                string box_form = string.Join("", pre);


                foreach (string sgl in pre)
                {
                    Queue<Double> dbl_prep = new Queue<double>();
                    //MessageBox.Show("NEW LINE");
                    foreach (var word in sgl.Split(' '))
                    {
                        if (word.Length > 5)
                        {
                            //MessageBox.Show(word);
                            dbl_prep.Enqueue(Convert.ToDouble(word));
                        }
                    }
                    if (dbl_prep.Count == 3)
                    {
                        masked_freq.Add(dbl_prep.Dequeue());
                        masked_re.Add(dbl_prep.Dequeue());
                        masked_im.Add(dbl_prep.Dequeue());
                    }
                    else
                    {
                        foreach (var word in dbl_prep)
                        {
                            MessageBox.Show("VALUE: " + word.ToString());
                        }
                    }
                }
                //Debug.WriteLine()
                nvyquist.Series[2].Points.DataBindXY(masked_re, masked_im);
            }
            catch (NullReferenceException)
            {
                MessageBox.Show("Bad path or Bad MPT file; Please Select a folder and a file");
            }
        }
        private void entire_fit_CheckedChanged(object sender, EventArgs e)
        {
            curr_mpt.Mask_choice = "4";
        }

        private void window_masker_CheckedChanged(object sender, EventArgs e)
        {
            try
            {
                curr_mpt.Mask_choice = "5";

                if (window_masker.Checked == true)
                {
                    nvyquist.ChartAreas[0].AxisX.Minimum = double.NaN;
                    nvyquist.ChartAreas[0].AxisY.Minimum = double.NaN;

                    nvyquist.ChartAreas[0].RecalculateAxesScale();

                    curr_mpt.X_min = nvyquist.ChartAreas[0].AxisX.ScaleView.ViewMinimum;
                    curr_mpt.X_max = nvyquist.ChartAreas[0].AxisX.ScaleView.ViewMaximum;
                    curr_mpt.Y_min = nvyquist.ChartAreas[0].AxisY.ScaleView.ViewMinimum;
                    curr_mpt.Y_max = nvyquist.ChartAreas[0].AxisY.ScaleView.ViewMaximum;


                    x_min.Text = nvyquist.ChartAreas[0].AxisX.ScaleView.ViewMinimum.ToString();
                    x_max.Text = nvyquist.ChartAreas[0].AxisX.ScaleView.ViewMaximum.ToString();
                    y_min.Text = nvyquist.ChartAreas[0].AxisY.ScaleView.ViewMinimum.ToString();
                    y_max.Text = nvyquist.ChartAreas[0].AxisY.ScaleView.ViewMaximum.ToString();
                }
                
            }
            catch (NullReferenceException)
            {
                MessageBox.Show("Please Fill in all four values to obtain a valid window.");
            }
        }


        private void masker_fit(string raw_path, string mpt_file, string masker_choice)
        {
            string[] masked_df = masked_mpt(raw_path, mpt_file, masker_choice);
            string[] output = masked_guesser(raw_path, mpt_file, masker_choice);
            List<string> pre = output.ToList();

            //Console.WriteLine(string.Join("\n", pre));
            string fit_label = pre[1];
            string fit_coeffs = pre[2];

            Console.WriteLine("0" + pre[0]);
            Console.WriteLine("1" + pre[1]);
            Console.WriteLine("2" + pre[2]);
            Console.WriteLine("3" + pre[3]);

            pre.RemoveRange(0, 3);

            string box_form = string.Join("\n", pre);
            //Console.WriteLine(box_form);
            string box_form_mpt = string.Join("", masked_df);
            fit_coeffs_box.AppendText(fit_coeffs);
            foreach (string sgl in pre)
            {
                Queue<Double> dbl_prep = new Queue<double>();
                foreach (var word in sgl.Split(','))
                {
                    if (word.Length > 1)
                    {
                        //MessageBox.Show("WORD: " + word);
                        dbl_prep.Enqueue(Convert.ToDouble(word));
                    }
                }
                if (dbl_prep.Count == 2)
                {
                    fit_re.Add(dbl_prep.Dequeue());
                    fit_im.Add(dbl_prep.Dequeue());
                }
                else
                {
                    foreach (var word in dbl_prep)
                    {
                        MessageBox.Show("Ununsual Value: " + word.ToString());
                    }
                }
            }
        }

        private void recal_fit(string raw_path, string mpt_file, string masker_choice, string indices)
        {
            string[] output = recal_guesser(raw_path, mpt_file, masker_choice, indices);
            
            List<string> pre = output.ToList();
            string fit_label = pre[1];
            string fit_coeffs = pre[2];
            //Console.WriteLine(fit_label);
            
            pre.RemoveRange(0, 2);
            string box_form = string.Join("\n", pre);
            //Console.WriteLine(box_form);
            //string box_form_mpt = string.Join("", masked_df);
            fit_coeffs_box.AppendText(fit_label);
            
            foreach (string sgl in pre)
            {
                Queue<Double> dbl_prep = new Queue<double>();
                foreach (var word in sgl.Split(','))
                {
                    if (word.Length > 1)
                    {
                        //MessageBox.Show("WORD: " + word);
                        dbl_prep.Enqueue(Convert.ToDouble(word));
                    }
                }
                if (dbl_prep.Count == 2)
                {
                    fit_re.Add(dbl_prep.Dequeue());
                    fit_im.Add(dbl_prep.Dequeue());
                }
                else
                {
                    foreach (var word in dbl_prep)
                    {
                        MessageBox.Show("Ununsual Value: " + word.ToString());
                    }
                }
            }  
        }


        private void window_masker_fit(string raw_path, string mpt_file, string xmin, string xmax, string ymin, string ymax)
        {
            //string[] masked_df = masked_mpt(raw_path, mpt_file, masker_choice);
            string[] output = window_masked_fit(raw_path, mpt_file, xmin, xmax, ymin, ymax);
            //string[] masked_df = window_mask
            List<string> pre = output.ToList();
            //MessageBox.Show(pre.Count.ToString());
            Console.WriteLine(string.Join("\n", pre));

            //Console.WriteLine(string.Join("\n", pre));
            string fit_label = pre[1];
            //string fit_coeffs = pre[2];
            //Console.WriteLine("0" + pre[0]);
            //Console.WriteLine("1" +  pre[1]);
            //Console.WriteLine("2" +  pre[2]);
            //Console.WriteLine("3" + pre[3]);

            pre.RemoveRange(0, 2);
            
            //string box_form = string.Join("", pre);
            fit_coeffs_box.AppendText(fit_label);

            foreach (string sgl in pre)
            {
                Queue<Double> dbl_prep = new Queue<double>();

                foreach (var word in sgl.Split(','))
                {
                    if (word.Length > 1)
                    {
                        //MessageBox.Show("WORD: " + word);
                        dbl_prep.Enqueue(Convert.ToDouble(word));
                    }
                }
                if (dbl_prep.Count == 2)
                {
                    fit_re.Add(dbl_prep.Dequeue());
                    fit_im.Add(dbl_prep.Dequeue());
                }
                else
                {
                    foreach (var word in dbl_prep)
                    {
                        MessageBox.Show("Ununsual Value: " + word.ToString());
                    }
                }
            }
            
        }

        private void recal_window_fit(string raw_path, string mpt_file, string xmin, string xmax, string ymin, string ymax, string indices)
        {
            //string[] masked_df = masked_mpt(raw_path, mpt_file, masker_choice);
            string[] output = recal_window_guesser(raw_path, mpt_file, xmin, xmax, ymin, ymax, indices);
            //string[] masked_df = window_mask
            List<string> pre = output.ToList();
            //MessageBox.Show(pre.Count.ToString());
            //Console.WriteLine(string.Join("\n", pre));
            string fit_label = pre[1];
            //string fit_coeffs = pre[2];

            pre.RemoveRange(0, 2);
            string box_form = string.Join("\n", pre);
            //Console.WriteLine(box_form);
            //string box_form_mpt = string.Join("", masked_df);
            fit_coeffs_box.AppendText(fit_label);

            foreach (string sgl in pre)
            {
                Queue<Double> dbl_prep = new Queue<double>();
                foreach (var word in sgl.Split(','))
                {
                    if (word.Length > 1)
                    {
                        //MessageBox.Show("WORD: " + word);
                        dbl_prep.Enqueue(Convert.ToDouble(word));
                    }
                }
                if (dbl_prep.Count == 2)
                {
                    fit_re.Add(dbl_prep.Dequeue());
                    fit_im.Add(dbl_prep.Dequeue());
                }
                else
                {
                    foreach (var word in dbl_prep)
                    {
                        MessageBox.Show("Ununsual Value: " + word.ToString());
                    }
                }
            }
        }


        private void fit_function_Click(object sender, EventArgs e)
        {


            fit_coeffs_box.Clear();
            nvyquist.Series[2].Points.Clear();
            nvyquist.Series[3].Points.Clear();

            string mpt_file = file_display_label.Text;
            string raw_path = curr_path;
            fit_re.Clear();
            fit_im.Clear();
            no_of_pts.Clear();

            //Console.WriteLine(curr_mpt.mpt_dict.Count().ToString());
            //bad_ints.Clear();

            if (entire_fit.Checked == true)
            {
                if (recalibrated)
                {
                    String indices = String.Concat("[" + String.Join(",", bad_ints.Select(item => item.ToString()).ToArray()) + "]");
                    
                    recal_fit(raw_path, mpt_file, "4", indices);
                }
                else
                {
                    //MessageBox.Show("HERE");
                    //MessageBox.Show(mpt_file, raw_path);
                    /*
                    string[] output = guesser(raw_path, mpt_file);
                    List<string> pre = output.ToList();
                    
                        
                    string fit_label = pre[0];
                    string fit_coeffs = pre[1];
                    pre.RemoveRange(0, 3);
                    fit_coeffs_box.AppendText(fit_coeffs);
                        
                      

                    string box_form = string.Join("", pre);

                    foreach (string sgl in pre)
                    {
                        Queue<Double> dbl_prep = new Queue<double>();
                        foreach (var word in sgl.Split(','))
                        {
                            if (word.Length > 1)
                            {
                                dbl_prep.Enqueue(Convert.ToDouble(word));
                            }
                        }
                        if (dbl_prep.Count == 2)
                        {
                            fit_re.Add(dbl_prep.Dequeue());
                            fit_im.Add(dbl_prep.Dequeue());
                        }
                        else
                        {
                            foreach (var word in dbl_prep)
                            {
                                MessageBox.Show("Ununsual Value: " + word.ToString());
                            }
                        }
                    }*/
                    masker_fit(raw_path, mpt_file, "4");
                }     
            }
            else if (masker1.Checked == true)
            {
                if (recalibrated)
                {
                    String indices = String.Concat("[" + String.Join(",", bad_ints.Select(item => item.ToString()).ToArray()) + "]");
                    //MessageBox.Show(indices);
                    recal_fit(raw_path, mpt_file, "1", indices);
                }
                else
                {
                    masker_fit(raw_path, mpt_file, "1");
                }
            }
            else if (masker2.Checked == true)
            {
                if (recalibrated)
                {
                    String indices = String.Concat("[" + String.Join(",", bad_ints.Select(item => item.ToString()).ToArray()) + "]");
                    recal_fit(raw_path, mpt_file, "2", indices);
                }
                else
                {
                    masker_fit(raw_path, mpt_file, "2");
                }
            }
            else if (masker3.Checked == true)
            {
                if (recalibrated)
                {
                    String indices = String.Concat("[" + String.Join(",", bad_ints.Select(item => item.ToString()).ToArray()) + "]");
                    //MessageBox.Show(indices);
                    recal_fit(raw_path, mpt_file, "3", indices);
                }
                else
                {
                    masker_fit(raw_path, mpt_file, "3");
                }
            }
            else if (window_masker.Checked == true)
            {
                x_min.Text = nvyquist.ChartAreas[0].AxisX.ScaleView.ViewMinimum.ToString();
                x_max.Text = nvyquist.ChartAreas[0].AxisX.ScaleView.ViewMaximum.ToString();
                y_min.Text = nvyquist.ChartAreas[0].AxisY.ScaleView.ViewMinimum.ToString();
                y_max.Text = nvyquist.ChartAreas[0].AxisY.ScaleView.ViewMaximum.ToString();
                if (recalibrated)
                {
                    String indices = String.Concat("[" + String.Join(",", bad_ints.Select(item => item.ToString()).ToArray()) + "]");
                    //MessageBox.Show(indices);
                    recal_window_fit(raw_path, mpt_file, x_min.Text, x_max.Text, y_min.Text, y_max.Text, indices);
                }
                else
                {
                    window_masker_fit(raw_path, mpt_file, x_min.Text, x_max.Text, y_min.Text, y_max.Text);
                }
            }
            else
            {
                MessageBox.Show("Bad Masking Choice");
            }
            
            if (fit_re.Count() > 0)
            {
                if (string.Join("", post_test).Length > 0)
                {
                    for (int counter = 0; counter < post_test.Length; counter++)
                    {
                        string striped = Regex.Replace(Regex.Replace(post_test[counter], @"\n", ""), @",", "");
                        if (striped == mpt_file)
                        {
                            post_test[counter] = ((striped + " FITTED\n"));
                        }
                        else
                        {
                            post_test[counter] = ((striped + "\n"));
                        }
                    }
                    temp = string.Join("", post_test);
                    path_list_box.Text = string.Join("", post_test);
                }
                else
                {
                    for (int counter = 0; counter < pre_test.Length; counter++)
                    {
                        string striped = Regex.Replace(Regex.Replace(pre_test[counter], @"\n", ""), @",", "");
                        if (striped == mpt_file)
                        {
                            post_test[counter] = ((striped + " FITTED\n"));
                        }
                        else
                        {
                            post_test[counter] = ((striped + "\n"));
                        }
                    }
                    temp = string.Join("", post_test);
                    path_list_box.Text = string.Join("", post_test);
                }
            }

            //Console.WriteLine(string.Join(", ", fit_re));
            no_of_pts.Text = (fit_re.Count().ToString() + " fitted values");
                

            nvyquist.Series[1].Points.DataBindXY(fit_re, fit_im);
            first_twenty.Series[1].Points.DataBindXY(fit_re.GetRange(0,20), fit_im.GetRange(0,20));

            foreach (string st0 in fit_coeffs_box.Lines)
            {
                //Console.WriteLine(st0);
                if (st0.Length > 0)
                {
                    
                    string new_line = Regex.Replace(st0, @"\s+", ", ");

                    string striped_line = Regex.Replace(new_line, "/", "");
                      
                    to_export.Add(striped_line);
                    string[] ls = striped_line.Split(',');
                    float x_int1 = float.Parse(ls[3]) + float.Parse(ls[7]);
                    float x_int2 = float.Parse(ls[2]) + float.Parse(ls[3]) + float.Parse(ls[7]);
                    nvyquist.Series[3].Points.AddXY(x_int1, 0);
                    nvyquist.Series[3].Points.AddXY(x_int2, 0);
                    
                    string r1 = String.Concat("R1 = ", ls[2]);
                    ls[2] = r1;
                    string r2 = String.Concat(" , R2 = ", ls[3]);
                    ls[3] = r2;
                    string n1 = String.Concat(" , N1 = ", ls[4]);
                    ls[4] = n1;
                    string fs1 = String.Concat(" , fs1 = ", ls[5]);
                    //ls[5] = fs1;
                    string q1 = String.Concat(" , Q1 = ", ls[6]);
                    ls[5] = q1;
                    string r3 = String.Concat(" , R3 = ", ls[7]);
                    ls[6] = r3;
                    string n2 = String.Concat(" , N2 = ", ls[8]);
                    ls[7] = n2;
                    string fs2 = String.Concat(" , fs2 = ", ls[9]);
                    //ls[9] = fs2;
                    string q2 = String.Concat(" , Q2 = ", ls[10]);
                    ls[8] = q2;
                    string q3 = String.Concat(" , Q3 = ", ls[11]);
                    ls[9] = q3;
                    string n3 = String.Concat(" , N3 = ", ls[12]);
                    ls[10] = n3;
                    fit_coeffs_box.Clear();
                    ls[0] = "";
                    ls[1] = "";
                    ls[11] = "";
                    ls[12] = "";
                    foreach(string str in ls)
                    {
                        fit_coeffs_box.AppendText(str);
                    }
                    fit_re.Clear();
                    fit_im.Clear();
                }
                else
                {
                    continue;
                }
                //Console.WriteLine("reached the strt of the fit coeffs organizer");
            }
        }
        private void timer1_Tick(object sender, EventArgs e)
        {
            
        }

        private void nvyquist_Click(object sender, EventArgs e)
        {
            
        }
        private void export_button_Click(object sender, EventArgs e)
        {
            string curr;
            int holder_ind;
            Dictionary<string, int> dupe_clearer = new Dictionary<string, int>();
            List<string> pre = new List<string>();

            to_export = to_export.Where(s => s.Length > 0).ToList();
            foreach(string str in to_export)
            {
                string[] lt = str.Split(',');
                curr = lt[1].ToString();
                holder_ind = to_export.IndexOf(str);
                if (dupe_clearer.ContainsKey(curr))
                {
                    dupe_clearer.Remove(curr);
                }
                dupe_clearer.Add(curr, holder_ind);
            }

            foreach (int val in dupe_clearer.Values)
            {
                pre.Add(to_export[val]);
            }
            if (saveFileDialog1.ShowDialog() == DialogResult.OK)
            {
                string filename = saveFileDialog1.FileName;
                File.WriteAllLines(filename, pre);
            }
        }
        private void checkbox_label_Click(object sender, EventArgs e)
        {
        }

        private void save_button_Click(object sender, EventArgs e)
        {
            saved_files.Add(curr_mpt);
        }
    }
}
