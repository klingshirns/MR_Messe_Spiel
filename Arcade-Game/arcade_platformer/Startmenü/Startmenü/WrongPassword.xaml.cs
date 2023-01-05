using System.Windows;

namespace Startmenü
{
    /// <summary>
    /// Interaktionslogik für WrongPassword.xaml
    /// </summary>
    public partial class WrongPassword : Window
    {
        public WrongPassword()
        {
            InitializeComponent();
        }

        private void Closebut_Click(object sender, RoutedEventArgs e)
        {
            this.Close();
        }
    }
}
