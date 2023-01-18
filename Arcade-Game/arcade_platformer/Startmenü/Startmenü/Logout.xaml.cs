using System.Windows;

namespace Startmenü
{
    /// <summary>
    /// Interaktionslogik für Logout.xaml
    /// </summary>
    public partial class Logout : Window
    {
        public Logout()
        {
            InitializeComponent();
        }

        private void Button_Click(object sender, RoutedEventArgs e)
        {
            this.Close();
        }

        private void Logoutbutton_Click(object sender, RoutedEventArgs e)
        {
            if (pasbox.Password == "4090")
            {
                Application.Current.Shutdown();
            }
            else if (pasbox.Password != "4090")
            {
                WrongPassword wrongPassword = new WrongPassword();
                wrongPassword.Show();
                pasbox.Clear();
            }
        }
    }
}