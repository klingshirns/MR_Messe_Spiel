using IronPython.Hosting;
using Microsoft.Scripting.Hosting;
using OpenXmlPowerTools;
using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Interop;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;

namespace Startmenü
{
    /// <summary>
    /// Interaktionslogik für MainWindow.xaml
    /// </summary>
    public partial class MainWindow : Window
    {
        //path to antimicro file
        public const string Filename = "..\\..\\..\\antimicro.exe";

        public MainWindow()
        {
            InitializeComponent();
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
            SettingWindow settingWindow = new SettingWindow();
            settingWindow.Show();
        }

        //game and antimicro will open
        private void Button_Click_2(object sender, RoutedEventArgs e)
        {
            Process.Start(Filename);
            /*var engine = Python.CreateEngine();
            engine.ExecuteFile("test2.py");*/
        }
    }
}
