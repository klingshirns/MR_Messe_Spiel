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

        private void Button_Click_1(object sender, RoutedEventArgs e)
        {
            string password = "1234";
            string logout = PasswordBox.TextInputEvent.ToString();
            if (logout == password)
            {
                Application.Current.Shutdown();
            }
            else
            {
                this.Close();
            }
        }
    }
}
