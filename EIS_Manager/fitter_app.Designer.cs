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
            System.Windows.Forms.DataVisualization.Charting.ChartArea chartArea2 = new System.Windows.Forms.DataVisualization.Charting.ChartArea();
            System.Windows.Forms.DataVisualization.Charting.Legend legend2 = new System.Windows.Forms.DataVisualization.Charting.Legend();
            System.Windows.Forms.DataVisualization.Charting.Series series3 = new System.Windows.Forms.DataVisualization.Charting.Series();
            System.Windows.Forms.DataVisualization.Charting.Series series4 = new System.Windows.Forms.DataVisualization.Charting.Series();
            this.pathbutton = new System.Windows.Forms.Button();
            this.dataframe_label = new System.Windows.Forms.Label();
            this.dataframe_box = new System.Windows.Forms.RichTextBox();
            this.title = new System.Windows.Forms.Label();
            this.logo = new System.Windows.Forms.PictureBox();
            this.error_box_label = new System.Windows.Forms.Label();
            this.error_box = new System.Windows.Forms.RichTextBox();
            this.x_max = new System.Windows.Forms.TextBox();
            this.x_min = new System.Windows.Forms.TextBox();
            this.file_display = new System.Windows.Forms.ComboBox();
            this.masker3 = new System.Windows.Forms.RadioButton();
            this.masker2 = new System.Windows.Forms.RadioButton();
            this.masker1 = new System.Windows.Forms.RadioButton();
            this.file_select = new System.Windows.Forms.Button();
            this.fit_function = new System.Windows.Forms.Button();
            this.folderBrowserDialog1 = new System.Windows.Forms.FolderBrowserDialog();
            this.folder_label = new System.Windows.Forms.Label();
            this.entire_fit = new System.Windows.Forms.RadioButton();
            this.y_min = new System.Windows.Forms.TextBox();
            this.y_max = new System.Windows.Forms.TextBox();
            this.window_masker = new System.Windows.Forms.RadioButton();
            this.mask_limit_label = new System.Windows.Forms.Label();
            this.mask_limits = new System.Windows.Forms.Label();
            this.freim_label = new System.Windows.Forms.Label();
            this.nvyquist = new System.Windows.Forms.DataVisualization.Charting.Chart();
            this.fit_coeffs_box = new System.Windows.Forms.RichTextBox();
            this.path_list_box = new System.Windows.Forms.RichTextBox();
            this.coeffs_label = new System.Windows.Forms.Label();
            this.file_display_label = new System.Windows.Forms.Label();
            this.exported_label = new System.Windows.Forms.Label();
            this.export_button = new System.Windows.Forms.Button();
            this.timer1 = new System.Windows.Forms.Timer(this.components);
            this.saveFileDialog1 = new System.Windows.Forms.SaveFileDialog();
            this.fit_coeffs_label = new System.Windows.Forms.Label();
            this.python_scripts = new System.Windows.Forms.Button();
            this.folderBrowserDialog2 = new System.Windows.Forms.FolderBrowserDialog();
            ((System.ComponentModel.ISupportInitialize)(this.logo)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.nvyquist)).BeginInit();
            this.SuspendLayout();
            // 
            // pathbutton
            // 
            this.pathbutton.Font = new System.Drawing.Font("Microsoft Sans Serif", 10F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.pathbutton.Location = new System.Drawing.Point(2, 113);
            this.pathbutton.Margin = new System.Windows.Forms.Padding(2);
            this.pathbutton.Name = "pathbutton";
            this.pathbutton.Size = new System.Drawing.Size(165, 22);
            this.pathbutton.TabIndex = 60;
            this.pathbutton.Text = "Select a Folder";
            this.pathbutton.UseVisualStyleBackColor = true;
            this.pathbutton.Click += new System.EventHandler(this.pathbutton_Click_1);
            // 
            // dataframe_label
            // 
            this.dataframe_label.AutoSize = true;
            this.dataframe_label.BackColor = System.Drawing.Color.MediumAquamarine;
            this.dataframe_label.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.dataframe_label.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.dataframe_label.ForeColor = System.Drawing.SystemColors.GrayText;
            this.dataframe_label.Location = new System.Drawing.Point(173, 39);
            this.dataframe_label.Name = "dataframe_label";
            this.dataframe_label.Size = new System.Drawing.Size(87, 22);
            this.dataframe_label.TabIndex = 59;
            this.dataframe_label.Text = "Dataframe";
            // 
            // dataframe_box
            // 
            this.dataframe_box.BackColor = System.Drawing.Color.MediumAquamarine;
            this.dataframe_box.Font = new System.Drawing.Font("Microsoft Sans Serif", 9F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.dataframe_box.Location = new System.Drawing.Point(173, 87);
            this.dataframe_box.Name = "dataframe_box";
            this.dataframe_box.ReadOnly = true;
            this.dataframe_box.Size = new System.Drawing.Size(290, 296);
            this.dataframe_box.TabIndex = 58;
            this.dataframe_box.Text = "";
            // 
            // title
            // 
            this.title.AutoSize = true;
            this.title.Font = new System.Drawing.Font("Microsoft Sans Serif", 11F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.title.Location = new System.Drawing.Point(2, 66);
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
            this.logo.Size = new System.Drawing.Size(165, 63);
            this.logo.SizeMode = System.Windows.Forms.PictureBoxSizeMode.StretchImage;
            this.logo.TabIndex = 54;
            this.logo.TabStop = false;
            // 
            // error_box_label
            // 
            this.error_box_label.AutoSize = true;
            this.error_box_label.BackColor = System.Drawing.Color.MistyRose;
            this.error_box_label.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.error_box_label.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.error_box_label.ForeColor = System.Drawing.SystemColors.ActiveCaption;
            this.error_box_label.Location = new System.Drawing.Point(173, 384);
            this.error_box_label.Name = "error_box_label";
            this.error_box_label.Size = new System.Drawing.Size(94, 22);
            this.error_box_label.TabIndex = 53;
            this.error_box_label.Text = "Fitting Error";
            // 
            // error_box
            // 
            this.error_box.BackColor = System.Drawing.Color.MistyRose;
            this.error_box.Font = new System.Drawing.Font("Microsoft Sans Serif", 9F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.error_box.Location = new System.Drawing.Point(173, 429);
            this.error_box.Name = "error_box";
            this.error_box.ReadOnly = true;
            this.error_box.Size = new System.Drawing.Size(296, 260);
            this.error_box.TabIndex = 37;
            this.error_box.Text = "";
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
            this.file_display.Location = new System.Drawing.Point(5, 140);
            this.file_display.Name = "file_display";
            this.file_display.Size = new System.Drawing.Size(162, 21);
            this.file_display.TabIndex = 43;
            this.file_display.Text = "Select MPT File";
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
            // file_select
            // 
            this.file_select.Location = new System.Drawing.Point(2, 167);
            this.file_select.Name = "file_select";
            this.file_select.Size = new System.Drawing.Size(165, 25);
            this.file_select.TabIndex = 39;
            this.file_select.Text = "Load MPT";
            this.file_select.UseVisualStyleBackColor = true;
            this.file_select.Click += new System.EventHandler(this.file_select_Click);
            // 
            // fit_function
            // 
            this.fit_function.Font = new System.Drawing.Font("Microsoft Sans Serif", 15F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.fit_function.Location = new System.Drawing.Point(5, 587);
            this.fit_function.Name = "fit_function";
            this.fit_function.Size = new System.Drawing.Size(143, 40);
            this.fit_function.TabIndex = 38;
            this.fit_function.Text = "FIT";
            this.fit_function.UseVisualStyleBackColor = true;
            this.fit_function.Click += new System.EventHandler(this.fit_function_Click);
            // 
            // folder_label
            // 
            this.folder_label.AutoSize = true;
            this.folder_label.BackColor = System.Drawing.Color.Tomato;
            this.folder_label.Font = new System.Drawing.Font("Microsoft Sans Serif", 8F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.folder_label.Location = new System.Drawing.Point(170, 4);
            this.folder_label.Name = "folder_label";
            this.folder_label.Size = new System.Drawing.Size(81, 13);
            this.folder_label.TabIndex = 62;
            this.folder_label.Text = "Selected Folder";
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
            // mask_limit_label
            // 
            this.mask_limit_label.AutoSize = true;
            this.mask_limit_label.BackColor = System.Drawing.SystemColors.GradientActiveCaption;
            this.mask_limit_label.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.mask_limit_label.Location = new System.Drawing.Point(2, 397);
            this.mask_limit_label.Margin = new System.Windows.Forms.Padding(2, 0, 2, 0);
            this.mask_limit_label.Name = "mask_limit_label";
            this.mask_limit_label.Size = new System.Drawing.Size(75, 13);
            this.mask_limit_label.TabIndex = 67;
            this.mask_limit_label.Text = "MASK LIMITS";
            // 
            // mask_limits
            // 
            this.mask_limits.AutoSize = true;
            this.mask_limits.BackColor = System.Drawing.SystemColors.GradientActiveCaption;
            this.mask_limits.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.mask_limits.Location = new System.Drawing.Point(2, 407);
            this.mask_limits.Margin = new System.Windows.Forms.Padding(2, 0, 2, 0);
            this.mask_limits.Name = "mask_limits";
            this.mask_limits.Size = new System.Drawing.Size(0, 13);
            this.mask_limits.TabIndex = 68;
            // 
            // freim_label
            // 
            this.freim_label.AutoSize = true;
            this.freim_label.BackColor = System.Drawing.Color.MediumAquamarine;
            this.freim_label.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.freim_label.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.freim_label.ForeColor = System.Drawing.SystemColors.GrayText;
            this.freim_label.Location = new System.Drawing.Point(173, 62);
            this.freim_label.Name = "freim_label";
            this.freim_label.Size = new System.Drawing.Size(244, 22);
            this.freim_label.TabIndex = 69;
            this.freim_label.Text = "Frequency       Real       Imaginary";
            // 
            // nvyquist
            // 
            chartArea2.Name = "ChartArea1";
            this.nvyquist.ChartAreas.Add(chartArea2);
            legend2.Name = "Legend1";
            this.nvyquist.Legends.Add(legend2);
            this.nvyquist.Location = new System.Drawing.Point(466, 0);
            this.nvyquist.Name = "nvyquist";
            this.nvyquist.Palette = System.Windows.Forms.DataVisualization.Charting.ChartColorPalette.Fire;
            series3.ChartArea = "ChartArea1";
            series3.ChartType = System.Windows.Forms.DataVisualization.Charting.SeriesChartType.Point;
            series3.Legend = "Legend1";
            series3.Name = "nvyquist";
            series4.ChartArea = "ChartArea1";
            series4.ChartType = System.Windows.Forms.DataVisualization.Charting.SeriesChartType.FastPoint;
            series4.Legend = "Legend1";
            series4.Name = "Fitted_Nyvquist";
            this.nvyquist.Series.Add(series3);
            this.nvyquist.Series.Add(series4);
            this.nvyquist.Size = new System.Drawing.Size(873, 572);
            this.nvyquist.TabIndex = 70;
            this.nvyquist.Text = "Full Graph";
            this.nvyquist.Click += new System.EventHandler(this.nvyquist_Click);
            // 
            // fit_coeffs_box
            // 
            this.fit_coeffs_box.BackColor = System.Drawing.Color.MistyRose;
            this.fit_coeffs_box.Font = new System.Drawing.Font("Microsoft Sans Serif", 10.5F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.fit_coeffs_box.Location = new System.Drawing.Point(466, 575);
            this.fit_coeffs_box.Name = "fit_coeffs_box";
            this.fit_coeffs_box.ReadOnly = true;
            this.fit_coeffs_box.Size = new System.Drawing.Size(873, 112);
            this.fit_coeffs_box.TabIndex = 71;
            this.fit_coeffs_box.Text = "";
            // 
            // path_list_box
            // 
            this.path_list_box.BackColor = System.Drawing.Color.LightSkyBlue;
            this.path_list_box.Font = new System.Drawing.Font("Microsoft Sans Serif", 7.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.path_list_box.Location = new System.Drawing.Point(2, 198);
            this.path_list_box.Name = "path_list_box";
            this.path_list_box.ReadOnly = true;
            this.path_list_box.Size = new System.Drawing.Size(165, 196);
            this.path_list_box.TabIndex = 61;
            this.path_list_box.Text = "Files to Fit";
            // 
            // coeffs_label
            // 
            this.coeffs_label.AutoSize = true;
            this.coeffs_label.BackColor = System.Drawing.Color.MistyRose;
            this.coeffs_label.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.coeffs_label.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.coeffs_label.ForeColor = System.Drawing.SystemColors.ActiveCaption;
            this.coeffs_label.Location = new System.Drawing.Point(173, 406);
            this.coeffs_label.Name = "coeffs_label";
            this.coeffs_label.Size = new System.Drawing.Size(231, 22);
            this.coeffs_label.TabIndex = 72;
            this.coeffs_label.Text = "Fitted Real       Fitted Imaginary";
            // 
            // file_display_label
            // 
            this.file_display_label.AutoSize = true;
            this.file_display_label.BackColor = System.Drawing.Color.Magenta;
            this.file_display_label.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.file_display_label.Location = new System.Drawing.Point(169, 19);
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
            this.export_button.Size = new System.Drawing.Size(143, 44);
            this.export_button.TabIndex = 75;
            this.export_button.Text = "Export Coefficients";
            this.export_button.UseVisualStyleBackColor = true;
            this.export_button.Click += new System.EventHandler(this.export_button_Click);
            // 
            // timer1
            // 
            this.timer1.Tick += new System.EventHandler(this.timer1_Tick);
            // 
            // fit_coeffs_label
            // 
            this.fit_coeffs_label.AutoSize = true;
            this.fit_coeffs_label.BackColor = System.Drawing.Color.MistyRose;
            this.fit_coeffs_label.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.fit_coeffs_label.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.fit_coeffs_label.ForeColor = System.Drawing.SystemColors.ActiveCaption;
            this.fit_coeffs_label.Location = new System.Drawing.Point(466, 550);
            this.fit_coeffs_label.Name = "fit_coeffs_label";
            this.fit_coeffs_label.Size = new System.Drawing.Size(140, 22);
            this.fit_coeffs_label.TabIndex = 76;
            this.fit_coeffs_label.Text = "Fitted Coefficients";
            // 
            // python_scripts
            // 
            this.python_scripts.Font = new System.Drawing.Font("Microsoft Sans Serif", 8F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.python_scripts.Location = new System.Drawing.Point(2, 87);
            this.python_scripts.Margin = new System.Windows.Forms.Padding(2);
            this.python_scripts.Name = "python_scripts";
            this.python_scripts.Size = new System.Drawing.Size(166, 22);
            this.python_scripts.TabIndex = 77;
            this.python_scripts.Text = "Select Python Scripts";
            this.python_scripts.UseVisualStyleBackColor = true;
            this.python_scripts.Click += new System.EventHandler(this.python_scripts_Click);
            // 
            // Fitter
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.BackColor = System.Drawing.SystemColors.Menu;
            this.ClientSize = new System.Drawing.Size(1339, 687);
            this.Controls.Add(this.python_scripts);
            this.Controls.Add(this.fit_coeffs_label);
            this.Controls.Add(this.export_button);
            this.Controls.Add(this.exported_label);
            this.Controls.Add(this.file_display_label);
            this.Controls.Add(this.coeffs_label);
            this.Controls.Add(this.fit_coeffs_box);
            this.Controls.Add(this.nvyquist);
            this.Controls.Add(this.freim_label);
            this.Controls.Add(this.mask_limits);
            this.Controls.Add(this.mask_limit_label);
            this.Controls.Add(this.window_masker);
            this.Controls.Add(this.y_max);
            this.Controls.Add(this.y_min);
            this.Controls.Add(this.error_box);
            this.Controls.Add(this.error_box_label);
            this.Controls.Add(this.entire_fit);
            this.Controls.Add(this.folder_label);
            this.Controls.Add(this.path_list_box);
            this.Controls.Add(this.pathbutton);
            this.Controls.Add(this.dataframe_label);
            this.Controls.Add(this.dataframe_box);
            this.Controls.Add(this.title);
            this.Controls.Add(this.logo);
            this.Controls.Add(this.x_max);
            this.Controls.Add(this.x_min);
            this.Controls.Add(this.file_display);
            this.Controls.Add(this.masker3);
            this.Controls.Add(this.masker2);
            this.Controls.Add(this.masker1);
            this.Controls.Add(this.file_select);
            this.Controls.Add(this.fit_function);
            this.Name = "Fitter";
            this.Text = "wildcat_fitter";
            this.Load += new System.EventHandler(this.Fitter_Load);
            ((System.ComponentModel.ISupportInitialize)(this.logo)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.nvyquist)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion
        private System.Windows.Forms.Button pathbutton;
        private System.Windows.Forms.Label dataframe_label;
        private System.Windows.Forms.RichTextBox dataframe_box;
        private System.Windows.Forms.Label title;
        private System.Windows.Forms.PictureBox logo;
        private System.Windows.Forms.Label error_box_label;
        private System.Windows.Forms.RichTextBox error_box;
        private System.Windows.Forms.TextBox x_max;
        private System.Windows.Forms.TextBox x_min;
        private System.Windows.Forms.ComboBox file_display;
        private System.Windows.Forms.RadioButton masker3;
        private System.Windows.Forms.RadioButton masker2;
        private System.Windows.Forms.RadioButton masker1;
        private System.Windows.Forms.Button file_select;
        private System.Windows.Forms.Button fit_function;
        private System.Windows.Forms.FolderBrowserDialog folderBrowserDialog1;
        private System.Windows.Forms.Label folder_label;
        private System.Windows.Forms.RadioButton entire_fit;
        private System.Windows.Forms.TextBox y_min;
        private System.Windows.Forms.TextBox y_max;
        private System.Windows.Forms.RadioButton window_masker;
        private System.Windows.Forms.Label mask_limit_label;
        private System.Windows.Forms.Label mask_limits;
        private System.Windows.Forms.Label freim_label;
        private System.Windows.Forms.DataVisualization.Charting.Chart nvyquist;
        private System.Windows.Forms.RichTextBox fit_coeffs_box;
        private System.Windows.Forms.RichTextBox path_list_box;
        private System.Windows.Forms.Label coeffs_label;
        private System.Windows.Forms.Label file_display_label;
        private System.Windows.Forms.Label exported_label;
        private System.Windows.Forms.Button export_button;
        private System.Windows.Forms.Timer timer1;
        private System.Windows.Forms.SaveFileDialog saveFileDialog1;
        private System.Windows.Forms.Label fit_coeffs_label;
        private System.Windows.Forms.Button python_scripts;
        private System.Windows.Forms.FolderBrowserDialog folderBrowserDialog2;
    }
}

