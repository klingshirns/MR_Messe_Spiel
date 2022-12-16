using System.Windows;

namespace Startmenü
{
    /// <summary>
    /// Interaktionslogik für Info1.xaml
    /// </summary>
    public partial class Info1 : Window
    {
        public Info1()
        {
            InitializeComponent();
        }

        private void Button_Click(object sender, RoutedEventArgs e)
        {
            this.Close();
        }
    }
}
