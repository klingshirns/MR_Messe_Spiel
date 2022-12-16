using System.Diagnostics;
using System.Windows;

namespace Startmenü
{
    /// <summary>
    /// Interaktionslogik für MainWindow.xaml
    /// </summary>
    public partial class MainWindow : Window
    {
        //path to antimicro file
        public const string Filename = @"..\..\..\..\..\..\Controller-Software\antimicro\antimicro.exe";

        public MainWindow()
        {
            InitializeComponent();
        }

        //game will be completely closed
        private void Button_Click(object sender, RoutedEventArgs e)
        {
            Logout logout = new Logout();
            logout.Show();

            MainWindow mainWindow = new MainWindow();
            mainWindow.AllowsTransparency = true;
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
            Process.Start(@"..\..\..\..\Python_Main_Game\main.py");
        }

        private void Testbu_Click(object sender, RoutedEventArgs e)
        {

        }
    }
}
