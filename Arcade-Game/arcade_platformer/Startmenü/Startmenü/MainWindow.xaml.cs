using DocumentFormat.OpenXml.Drawing;
using System.Diagnostics;
using System.Windows;
using System;
using System.IO;
namespace Startmenü
{
    /// <summary>
    /// Interaktionslogik für MainWindow.xaml
    /// </summary>
    public partial class MainWindow : Window
    {
        private readonly string currentDir;

        public MainWindow()
        {
            InitializeComponent();
            currentDir = System.IO.Directory.GetCurrentDirectory();
        }

        //game will be completely closed
        private void Button_Click(object sender, RoutedEventArgs e)
        {
            Logout logout = new Logout();
            logout.Show();
        }

        //Settings will open
        private void Button_Click_1(object sender, RoutedEventArgs e)
        {
            Directory.SetCurrentDirectory(currentDir);
            SettingWindow settingWindow = new SettingWindow();
            settingWindow.Show();
        }

        //game and antimicro will open
        private void Button_Click_2(object sender, RoutedEventArgs e)
        {
            Directory.SetCurrentDirectory(currentDir);

            string mainDir = @"..\..\..\..\Python_Main_Game";
            string mainExe = @"main";
            string antimicro = @"..\..\..\..\..\..\Controller-Software\antimicro\antimicro.exe";

            Process.Start(antimicro);

            // Set current directory where main.exe for the game is located 
            Directory.SetCurrentDirectory(mainDir);

            // var fullpath = System.IO.Path.Combine(mainDir, mainExe);

            Process main = new Process();
            main.StartInfo.FileName = mainExe;
            main.Start();
        }
    }
}