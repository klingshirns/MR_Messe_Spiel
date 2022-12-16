using System.Windows;

namespace Startmenü
{
    /// <summary>
    /// Interaktionslogik für Hedgewindow.xaml
    /// </summary>
    public partial class Hedgewindow : Window
    {
        public Hedgewindow()
        {
            InitializeComponent();
        }

        private void Button_Click(object sender, RoutedEventArgs e)
        {
            this.Close();
        }
    }
}
