using Microsoft.Web.Mvc.Controls;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Shapes;
using System.Windows.Threading;

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
            if (pasbox.Password == "1111")
            {
                Application.Current.Shutdown();
            }
            else if(pasbox.Password != "1111")
            {
                WrongPassword wrongPassword = new WrongPassword();
                wrongPassword.Show();
                pasbox.Clear();
            }
        }
    }
}