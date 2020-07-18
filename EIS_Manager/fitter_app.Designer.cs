namespace EIS_Manager
{
    partial class Fitter
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.components = new System.ComponentModel.Container();
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(Fitter));
            System.Windows.Forms.DataVisualization.Charting.ChartArea chartArea3 = new System.Windows.Forms.DataVisualization.Charting.ChartArea();
            System.Windows.Forms.DataVisualization.Charting.Legend legend3 = new System.Windows.Forms.DataVisualization.Charting.Legend();
            System.Windows.Forms.DataVisualization.Charting.Series series7 = new System.Windows.Forms.DataVisualization.Charting.Series();
            System.Windows.Forms.DataVisualization.Charting.Series series8 = new System.Windows.Forms.DataVisualization.Charting.Series();
            System.Windows.Forms.DataVisualization.Charting.Series series9 = new System.Windows.Forms.DataVisualization.Charting.Series();
            System.Windows.Forms.DataVisualization.Charting.Series series10 = new System.Windows.Forms.DataVisualization.Charting.Series();
            System.Windows.Forms.DataVisualization.Charting.ChartArea chartArea4 = new System.Windows.Forms.DataVisualization.Charting.ChartArea();
            System.Windows.Forms.DataVisualization.Charting.Legend legend4 = new System.Windows.Forms.DataVisualization.Charting.Legend();
            System.Windows.Forms.DataVisualization.Charting.Series series11 = new System.Windows.Forms.DataVisualization.Charting.Series();
            System.Windows.Forms.DataVisualization.Charting.Series series12 = new System.Windows.Forms.DataVisualization.Charting.Series();
            this.pathbutton = new System.Windows.Forms.Button();
            this.title = new System.Windows.Forms.Label();
            this.logo = new System.Windows.Forms.PictureBox();
            this.x_max = new System.Windows.Forms.TextBox();
            this.x_min = new System.Windows.Forms.TextBox();
            this.file_display = new System.Windows.Forms.ComboBox();
            this.masker3 = new System.Windows.Forms.RadioButton();
            this.masker2 = new System.Windows.Forms.RadioButton();
            this.masker1 = new System.Windows.Forms.RadioButton();
            this.fit_function = new System.Windows.Forms.Button();
            this.folderBrowserDialog1 = new System.Windows.Forms.FolderBrowserDialog();
            this.entire_fit = new System.Windows.Forms.RadioButton();
            this.y_min = new System.Windows.Forms.TextBox();
            this.y_max = new System.Windows.Forms.TextBox();
            this.window_masker = new System.Windows.Forms.RadioButton();
            this.nvyquist = new System.Windows.Forms.DataVisualization.Charting.Chart();
            this.fit_coeffs_box = new System.Windows.Forms.RichTextBox();
            this.path_list_box = new System.Windows.Forms.RichTextBox();
            this.file_display_label = new System.Windows.Forms.Label();
            this.exported_label = new System.Windows.Forms.Label();
            this.export_button = new System.Windows.Forms.Button();
            this.timer1 = new System.Windows.Forms.Timer(this.components);
            this.saveFileDialog1 = new System.Windows.Forms.SaveFileDialog();
            this.python_scripts = new System.Windows.Forms.Button();
            this.folderBrowserDialog2 = new System.Windows.Forms.FolderBrowserDialog();
            this.first_twenty = new System.Windows.Forms.DataVisualization.Charting.Chart();
            this.df_checkbox = new System.Windows.Forms.CheckedListBox();
            this.recal_button = new System.Windows.Forms.Button();
            this.checkbox_label = new System.Windows.Forms.Label();
            this.label1 = new System.Windows.Forms.Label();
            this.gen_graph_label = new System.Windows.Forms.Label();
            this.save_button = new System.Windows.Forms.Button();
            this.no_of_pts = new System.Windows.Forms.RichTextBox();
            this.saveFileDialog2 = new System.Windows.Forms.SaveFileDialog();
            this.export_settings_button = new System.Windows.Forms.Button();
            ((System.ComponentModel.ISupportInitialize)(this.logo)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.nvyquist)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.first_twenty)).BeginInit();
            this.SuspendLayout();
            // 
            // pathbutton
            // 
            this.pathbutton.Font = new System.Drawing.Font("Microsoft Sans Serif", 10F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.pathbutton.Location = new System.Drawing.Point(1, 113);
            this.pathbutton.Margin = new System.Windows.Forms.Padding(2);
            this.pathbutton.Name = "pathbutton";
            this.pathbutton.Size = new System.Drawing.Size(162, 22);
            this.pathbutton.TabIndex = 60;
            this.pathbutton.Text = "Select a Folder";
            this.pathbutton.UseVisualStyleBackColor = true;
            this.pathbutton.Click += new System.EventHandler(this.pathbutton_Click_1);
            // 
            // title
            // 
            this.title.AutoSize = true;
            this.title.Font = new System.Drawing.Font("Microsoft Sans Serif", 11F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.title.Location = new System.Drawing.Point(-1, 66);
            this.title.Name = "title";
            this.title.Size = new System.Drawing.Size(110, 18);
            this.title.TabIndex = 55;
            this.title.Text = "Wildcat E.I.S.";
            // 
            // logo
            // 
            this.logo.BackColor = System.Drawing.Color.Transparent;
            this.logo.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.logo.Image = ((System.Drawing.Image)(resources.GetObject("logo.Image")));
            this.logo.Location = new System.Drawing.Point(2, 0);
            this.logo.Name = "logo";
            this.logo.Size = new System.Drawing.Size(161, 63);
            this.logo.SizeMode = System.Windows.Forms.PictureBoxSizeMode.StretchImage;
            this.logo.TabIndex = 54;
            this.logo.TabStop = false;
            // 
            // x_max
            // 
            this.x_max.Enabled = false;
            this.x_max.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.x_max.Location = new System.Drawing.Point(67, 543);
            this.x_max.Name = "x_max";
            this.x_max.Size = new System.Drawing.Size(60, 20);
            this.x_max.TabIndex = 45;
            this.x_max.Text = "X Max";
            // 
            // x_min
            // 
            this.x_min.Enabled = false;
            this.x_min.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.x_min.Location = new System.Drawing.Point(5, 543);
            this.x_min.Name = "x_min";
            this.x_min.Size = new System.Drawing.Size(56, 20);
            this.x_min.TabIndex = 44;
            this.x_min.Text = "X min";
            // 
            // file_display
            // 
            this.file_display.FormattingEnabled = true;
            this.file_display.Items.AddRange(new object[] {
            "option1",
            "option2"});
            this.file_display.Location = new System.Drawing.Point(1, 140);
            this.file_display.Name = "file_display";
            this.file_display.Size = new System.Drawing.Size(162, 21);
            this.file_display.TabIndex = 43;
            this.file_display.Text = "Select MPT File";
            this.file_display.SelectedIndexChanged += new System.EventHandler(this.file_display_SelectedIndexChanged);
            // 
            // masker3
            // 
            this.masker3.AutoSize = true;
            this.masker3.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.masker3.Location = new System.Drawing.Point(5, 475);
            this.masker3.Name = "masker3";
            this.masker3.Size = new System.Drawing.Size(69, 17);
            this.masker3.TabIndex = 42;
            this.masker3.Text = "Masker 3";
            this.masker3.UseVisualStyleBackColor = true;
            this.masker3.CheckedChanged += new System.EventHandler(this.masker3_CheckedChanged);
            // 
            // masker2
            // 
            this.masker2.AutoSize = true;
            this.masker2.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.masker2.Location = new System.Drawing.Point(5, 452);
            this.masker2.Name = "masker2";
            this.masker2.Size = new System.Drawing.Size(69, 17);
            this.masker2.TabIndex = 41;
            this.masker2.Text = "Masker 2";
            this.masker2.UseVisualStyleBackColor = true;
            this.masker2.CheckedChanged += new System.EventHandler(this.masker2_CheckedChanged);
            // 
            // masker1
            // 
            this.masker1.AutoSize = true;
            this.masker1.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.masker1.Location = new System.Drawing.Point(5, 429);
            this.masker1.Name = "masker1";
            this.masker1.Size = new System.Drawing.Size(69, 17);
            this.masker1.TabIndex = 40;
            this.masker1.Text = "Masker 1";
            this.masker1.UseVisualStyleBackColor = true;
            this.masker1.CheckedChanged += new System.EventHandler(this.masker1_CheckedChanged);
            // 
            // fit_function
            // 
            this.fit_function.Font = new System.Drawing.Font("Microsoft Sans Serif", 15F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.fit_function.Location = new System.Drawing.Point(5, 587);
            this.fit_function.Name = "fit_function";
            this.fit_function.Size = new System.Drawing.Size(68, 40);
            this.fit_function.TabIndex = 38;
            this.fit_function.Text = "FIT";
            this.fit_function.UseVisualStyleBackColor = true;
            this.fit_function.Click += new System.EventHandler(this.fit_function_Click);
            // 
            // entire_fit
            // 
            this.entire_fit.AutoSize = true;
            this.entire_fit.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.entire_fit.Location = new System.Drawing.Point(5, 498);
            this.entire_fit.Name = "entire_fit";
            this.entire_fit.Size = new System.Drawing.Size(68, 17);
            this.entire_fit.TabIndex = 63;
            this.entire_fit.Text = "No Mask";
            this.entire_fit.UseVisualStyleBackColor = true;
            this.entire_fit.CheckedChanged += new System.EventHandler(this.entire_fit_CheckedChanged);
            // 
            // y_min
            // 
            this.y_min.Enabled = false;
            this.y_min.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.y_min.Location = new System.Drawing.Point(5, 561);
            this.y_min.Name = "y_min";
            this.y_min.Size = new System.Drawing.Size(56, 20);
            this.y_min.TabIndex = 64;
            this.y_min.Text = "Y Min";
            // 
            // y_max
            // 
            this.y_max.Enabled = false;
            this.y_max.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.y_max.Location = new System.Drawing.Point(67, 561);
            this.y_max.Name = "y_max";
            this.y_max.Size = new System.Drawing.Size(60, 20);
            this.y_max.TabIndex = 65;
            this.y_max.Text = "Y Max";
            // 
            // window_masker
            // 
            this.window_masker.AutoSize = true;
            this.window_masker.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.window_masker.Location = new System.Drawing.Point(5, 521);
            this.window_masker.Name = "window_masker";
            this.window_masker.Size = new System.Drawing.Size(102, 17);
            this.window_masker.TabIndex = 66;
            this.window_masker.Text = "Window Masker";
            this.window_masker.UseVisualStyleBackColor = true;
            this.window_masker.CheckedChanged += new System.EventHandler(this.window_masker_CheckedChanged);
            // 
            // nvyquist
            // 
            chartArea3.Name = "ChartArea1";
            this.nvyquist.ChartAreas.Add(chartArea3);
            legend3.Name = "Legend1";
            this.nvyquist.Legends.Add(legend3);
            this.nvyquist.Location = new System.Drawing.Point(168, 0);
            this.nvyquist.Name = "nvyquist";
            this.nvyquist.Palette = System.Windows.Forms.DataVisualization.Charting.ChartColorPalette.EarthTones;
            series7.ChartArea = "ChartArea1";
            series7.ChartType = System.Windows.Forms.DataVisualization.Charting.SeriesChartType.FastPoint;
            series7.Legend = "Legend1";
            series7.MarkerSize = 10;
            series7.Name = "nvyquist";
            series8.ChartArea = "ChartArea1";
            series8.ChartType = System.Windows.Forms.DataVisualization.Charting.SeriesChartType.FastPoint;
            series8.Legend = "Legend1";
            series8.MarkerSize = 10;
            series8.Name = "Fitted_Nyvquist";
            series9.ChartArea = "ChartArea1";
            series9.ChartType = System.Windows.Forms.DataVisualization.Charting.SeriesChartType.FastPoint;
            series9.Legend = "Legend1";
            series9.MarkerSize = 10;
            series9.Name = "masked";
            series10.ChartArea = "ChartArea1";
            series10.ChartType = System.Windows.Forms.DataVisualization.Charting.SeriesChartType.FastPoint;
            series10.Legend = "Legend1";
            series10.MarkerSize = 15;
            series10.Name = "x_ints";
            this.nvyquist.Series.Add(series7);
            this.nvyquist.Series.Add(series8);
            this.nvyquist.Series.Add(series9);
            this.nvyquist.Series.Add(series10);
            this.nvyquist.Size = new System.Drawing.Size(771, 675);
            this.nvyquist.TabIndex = 70;
            this.nvyquist.Text = "Full Graph";
            this.nvyquist.Click += new System.EventHandler(this.nvyquist_Click);
            // 
            // fit_coeffs_box
            // 
            this.fit_coeffs_box.BackColor = System.Drawing.Color.MistyRose;
            this.fit_coeffs_box.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.fit_coeffs_box.Location = new System.Drawing.Point(172, 647);
            this.fit_coeffs_box.Name = "fit_coeffs_box";
            this.fit_coeffs_box.ReadOnly = true;
            this.fit_coeffs_box.Size = new System.Drawing.Size(986, 40);
            this.fit_coeffs_box.TabIndex = 71;
            this.fit_coeffs_box.Text = "";
            // 
            // path_list_box
            // 
            this.path_list_box.BackColor = System.Drawing.Color.LightSkyBlue;
            this.path_list_box.Font = new System.Drawing.Font("Microsoft Sans Serif", 7.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.path_list_box.Location = new System.Drawing.Point(0, 187);
            this.path_list_box.Name = "path_list_box";
            this.path_list_box.ReadOnly = true;
            this.path_list_box.Size = new System.Drawing.Size(162, 236);
            this.path_list_box.TabIndex = 61;
            this.path_list_box.Text = "Files to Fit";
            // 
            // file_display_label
            // 
            this.file_display_label.AutoSize = true;
            this.file_display_label.BackColor = System.Drawing.Color.Magenta;
            this.file_display_label.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.file_display_label.Location = new System.Drawing.Point(1, 164);
            this.file_display_label.Name = "file_display_label";
            this.file_display_label.Size = new System.Drawing.Size(101, 20);
            this.file_display_label.TabIndex = 73;
            this.file_display_label.Text = "Selected File";
            // 
            // exported_label
            // 
            this.exported_label.AutoSize = true;
            this.exported_label.BackColor = System.Drawing.Color.DarkOrange;
            this.exported_label.Font = new System.Drawing.Font("Microsoft Sans Serif", 8F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.exported_label.Location = new System.Drawing.Point(308, 28);
            this.exported_label.Name = "exported_label";
            this.exported_label.Size = new System.Drawing.Size(0, 13);
            this.exported_label.TabIndex = 74;
            // 
            // export_button
            // 
            this.export_button.ForeColor = System.Drawing.Color.Red;
            this.export_button.Location = new System.Drawing.Point(5, 632);
            this.export_button.Margin = new System.Windows.Forms.Padding(2);
            this.export_button.Name = "export_button";
            this.export_button.Size = new System.Drawing.Size(69, 44);
            this.export_button.TabIndex = 75;
            this.export_button.Text = "Export Coefficients";
            this.export_button.UseVisualStyleBackColor = true;
            this.export_button.Click += new System.EventHandler(this.export_button_Click);
            // 
            // timer1
            // 
            this.timer1.Tick += new System.EventHandler(this.timer1_Tick);
            // 
            // python_scripts
            // 
            this.python_scripts.Font = new System.Drawing.Font("Microsoft Sans Serif", 8F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.python_scripts.Location = new System.Drawing.Point(1, 87);
            this.python_scripts.Margin = new System.Windows.Forms.Padding(2);
            this.python_scripts.Name = "python_scripts";
            this.python_scripts.Size = new System.Drawing.Size(162, 22);
            this.python_scripts.TabIndex = 77;
            this.python_scripts.Text = "Select Python Scripts";
            this.python_scripts.UseVisualStyleBackColor = true;
            this.python_scripts.Click += new System.EventHandler(this.python_scripts_Click);
            // 
            // first_twenty
            // 
            chartArea4.Name = "ChartArea1";
            this.first_twenty.ChartAreas.Add(chartArea4);
            legend4.Name = "Legend1";
            this.first_twenty.Legends.Add(legend4);
            this.first_twenty.Location = new System.Drawing.Point(760, 87);
            this.first_twenty.Name = "first_twenty";
            series11.ChartArea = "ChartArea1";
            series11.ChartType = System.Windows.Forms.DataVisualization.Charting.SeriesChartType.FastPoint;
            series11.Legend = "Legend1";
            series11.MarkerSize = 10;
            series11.Name = "Fitted_Nyvquist";
            series12.ChartArea = "ChartArea1";
            series12.ChartType = System.Windows.Forms.DataVisualization.Charting.SeriesChartType.Point;
            series12.Legend = "Legend1";
            series12.MarkerSize = 10;
            series12.Name = "nvyquist";
            this.first_twenty.Series.Add(series11);
            this.first_twenty.Series.Add(series12);
            this.first_twenty.Size = new System.Drawing.Size(567, 554);
            this.first_twenty.TabIndex = 78;
            this.first_twenty.Text = "Full Graph";
            // 
            // df_checkbox
            // 
            this.df_checkbox.BackColor = System.Drawing.Color.BlanchedAlmond;
            this.df_checkbox.FormattingEnabled = true;
            this.df_checkbox.Location = new System.Drawing.Point(1172, 169);
            this.df_checkbox.Name = "df_checkbox";
            this.df_checkbox.Size = new System.Drawing.Size(167, 439);
            this.df_checkbox.TabIndex = 79;
            // 
            // recal_button
            // 
            this.recal_button.Location = new System.Drawing.Point(1172, 618);
            this.recal_button.Name = "recal_button";
            this.recal_button.Size = new System.Drawing.Size(167, 23);
            this.recal_button.TabIndex = 80;
            this.recal_button.Text = "Recalibrate";
            this.recal_button.UseVisualStyleBackColor = true;
            this.recal_button.Click += new System.EventHandler(this.recal_button_Click);
            // 
            // checkbox_label
            // 
            this.checkbox_label.AutoSize = true;
            this.checkbox_label.BackColor = System.Drawing.Color.BlanchedAlmond;
            this.checkbox_label.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, ((System.Drawing.FontStyle)((System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic))), System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.checkbox_label.ForeColor = System.Drawing.SystemColors.ControlText;
            this.checkbox_label.Location = new System.Drawing.Point(1168, 146);
            this.checkbox_label.Name = "checkbox_label";
            this.checkbox_label.Size = new System.Drawing.Size(150, 20);
            this.checkbox_label.TabIndex = 81;
            this.checkbox_label.Text = "Recalibration Box";
            this.checkbox_label.Click += new System.EventHandler(this.checkbox_label_Click);
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.BackColor = System.Drawing.Color.Snow;
            this.label1.Font = new System.Drawing.Font("Microsoft Sans Serif", 14.25F, ((System.Drawing.FontStyle)((System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic))), System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.label1.ForeColor = System.Drawing.SystemColors.ControlText;
            this.label1.Location = new System.Drawing.Point(934, 39);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(224, 24);
            this.label1.TabIndex = 82;
            this.label1.Text = "High Frequency Graph";
            // 
            // gen_graph_label
            // 
            this.gen_graph_label.AutoSize = true;
            this.gen_graph_label.BackColor = System.Drawing.Color.Snow;
            this.gen_graph_label.Font = new System.Drawing.Font("Microsoft Sans Serif", 14.25F, ((System.Drawing.FontStyle)((System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic))), System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.gen_graph_label.ForeColor = System.Drawing.SystemColors.ControlText;
            this.gen_graph_label.Location = new System.Drawing.Point(446, 0);
            this.gen_graph_label.Name = "gen_graph_label";
            this.gen_graph_label.Size = new System.Drawing.Size(108, 24);
            this.gen_graph_label.TabIndex = 83;
            this.gen_graph_label.Text = "Full Graph";
            // 
            // save_button
            // 
            this.save_button.Font = new System.Drawing.Font("Microsoft Sans Serif", 15F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.save_button.Location = new System.Drawing.Point(74, 587);
            this.save_button.Name = "save_button";
            this.save_button.Size = new System.Drawing.Size(88, 40);
            this.save_button.TabIndex = 84;
            this.save_button.Text = "SAVE";
            this.save_button.UseVisualStyleBackColor = true;
            this.save_button.Click += new System.EventHandler(this.save_button_Click);
            // 
            // no_of_pts
            // 
            this.no_of_pts.BackColor = System.Drawing.Color.LightGreen;
            this.no_of_pts.Font = new System.Drawing.Font("Microsoft Sans Serif", 14.25F, ((System.Drawing.FontStyle)((System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic))), System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.no_of_pts.Location = new System.Drawing.Point(1172, 647);
            this.no_of_pts.Name = "no_of_pts";
            this.no_of_pts.ReadOnly = true;
            this.no_of_pts.Size = new System.Drawing.Size(167, 40);
            this.no_of_pts.TabIndex = 85;
            this.no_of_pts.Text = "";
            // 
            // export_settings_button
            // 
            this.export_settings_button.ForeColor = System.Drawing.Color.SteelBlue;
            this.export_settings_button.ImageAlign = System.Drawing.ContentAlignment.TopCenter;
            this.export_settings_button.Location = new System.Drawing.Point(74, 631);
            this.export_settings_button.Margin = new System.Windows.Forms.Padding(2);
            this.export_settings_button.Name = "export_settings_button";
            this.export_settings_button.Size = new System.Drawing.Size(88, 44);
            this.export_settings_button.TabIndex = 86;
            this.export_settings_button.Text = "Export Settings";
            this.export_settings_button.UseVisualStyleBackColor = true;
            this.export_settings_button.Click += new System.EventHandler(this.export_settings_button_Click);
            // 
            // Fitter
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.BackColor = System.Drawing.Color.White;
            this.ClientSize = new System.Drawing.Size(1339, 687);
            this.Controls.Add(this.export_settings_button);
            this.Controls.Add(this.no_of_pts);
            this.Controls.Add(this.save_button);
            this.Controls.Add(this.gen_graph_label);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.checkbox_label);
            this.Controls.Add(this.recal_button);
            this.Controls.Add(this.df_checkbox);
            this.Controls.Add(this.first_twenty);
            this.Controls.Add(this.python_scripts);
            this.Controls.Add(this.export_button);
            this.Controls.Add(this.exported_label);
            this.Controls.Add(this.file_display_label);
            this.Controls.Add(this.fit_coeffs_box);
            this.Controls.Add(this.nvyquist);
            this.Controls.Add(this.window_masker);
            this.Controls.Add(this.y_max);
            this.Controls.Add(this.y_min);
            this.Controls.Add(this.entire_fit);
            this.Controls.Add(this.path_list_box);
            this.Controls.Add(this.pathbutton);
            this.Controls.Add(this.title);
            this.Controls.Add(this.logo);
            this.Controls.Add(this.x_max);
            this.Controls.Add(this.x_min);
            this.Controls.Add(this.file_display);
            this.Controls.Add(this.masker3);
            this.Controls.Add(this.masker2);
            this.Controls.Add(this.masker1);
            this.Controls.Add(this.fit_function);
            this.Name = "Fitter";
            this.Text = "wildcat_fitter";
            this.Load += new System.EventHandler(this.Fitter_Load);
            ((System.ComponentModel.ISupportInitialize)(this.logo)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.nvyquist)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.first_twenty)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion
        private System.Windows.Forms.Button pathbutton;
        private System.Windows.Forms.Label title;
        private System.Windows.Forms.PictureBox logo;
        private System.Windows.Forms.TextBox x_max;
        private System.Windows.Forms.TextBox x_min;
        private System.Windows.Forms.ComboBox file_display;
        private System.Windows.Forms.RadioButton masker3;
        private System.Windows.Forms.RadioButton masker2;
        private System.Windows.Forms.RadioButton masker1;
        private System.Windows.Forms.Button fit_function;
        private System.Windows.Forms.FolderBrowserDialog folderBrowserDialog1;
        private System.Windows.Forms.RadioButton entire_fit;
        private System.Windows.Forms.TextBox y_min;
        private System.Windows.Forms.TextBox y_max;
        private System.Windows.Forms.RadioButton window_masker;
        private System.Windows.Forms.DataVisualization.Charting.Chart nvyquist;
        private System.Windows.Forms.RichTextBox fit_coeffs_box;
        private System.Windows.Forms.RichTextBox path_list_box;
        private System.Windows.Forms.Label file_display_label;
        private System.Windows.Forms.Label exported_label;
        private System.Windows.Forms.Button export_button;
        private System.Windows.Forms.Timer timer1;
        private System.Windows.Forms.SaveFileDialog saveFileDialog1;
        private System.Windows.Forms.Button python_scripts;
        private System.Windows.Forms.FolderBrowserDialog folderBrowserDialog2;
        private System.Windows.Forms.DataVisualization.Charting.Chart first_twenty;
        private System.Windows.Forms.CheckedListBox df_checkbox;
        private System.Windows.Forms.Button recal_button;
        private System.Windows.Forms.Label checkbox_label;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Label gen_graph_label;
        private System.Windows.Forms.Button save_button;
        private System.Windows.Forms.RichTextBox no_of_pts;
        private System.Windows.Forms.SaveFileDialog saveFileDialog2;
        private System.Windows.Forms.Button export_settings_button;
    }
}

