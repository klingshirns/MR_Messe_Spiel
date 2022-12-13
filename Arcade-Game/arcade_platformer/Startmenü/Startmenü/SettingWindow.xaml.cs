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
using System.IO;
using Nancy.Json;
using System.Threading;

namespace Startmenü
{
    /// <summary>
    /// Interaktionslogik für SettingWindow.xaml
    /// </summary>
    public partial class SettingWindow : Window
    {
        //path to player.json
        private readonly string path = @"..\..\..\..\json\player.json";

        private SettingDto setting;

        public SettingWindow()
        {
            InitializeComponent();
            setting = ReadJason();

            if (setting.SelectedPlayer == 0)
            {
                Button_Click_6(null, null);
            }
            if (setting.SelectedPlayer == 1)
            {
                ChoosButton2_Click(null, null);
            }
            if (setting.SelectedPlayer == 2)
            {
                ChoosButton3_Click(null, null);
            }
            if (setting.SelectedPlayer == 3)
            {
                ChoosButton4_Click(null, null);
            }

        }
        //Save Settings and changes the player.json
        private void Save_Click(object sender, RoutedEventArgs e)
        {
            WriteJson();
        }
        //Settings will be closed
        private void Exitbut_Click_1(object sender, RoutedEventArgs e)
        {
            this.Close();
        }

        //Info of "Einfachmacher" will open
        private void Button_Click_2(object sender, RoutedEventArgs e)
        {
            Info1 info1 = new Info1();
            info1.Show();
        }

        //Info of "Vorangeher" will open
        private void Button_Click_3(object sender, RoutedEventArgs e)
        {
            Info2 info2 = new Info2();
            info2.Show();
        }

        //Info of "Kundenversteher" will open
        private void Button_Click_4(object sender, RoutedEventArgs e)
        {
            Info3 info3 = new Info3();
            info3.Show();
        }

        //Info of "Zusammenbringer" will open
        private void Button_Click_5(object sender, RoutedEventArgs e)
        {
            Info4 info4 = new Info4();
            info4.Show();
        }

        private void Button_Click_6(object sender, RoutedEventArgs e)
        {
            label.Content = "Technische Ausbildung:\n - eindeutige Prioritäten\n - setzten auf 80 Prozent Lösungen und verbessern bei Bedarf\n - Lösungen klein und kompakt, kein Schnickschnack\n - denken und handeln ergebnisorientiert\n";

            setting.SelectedPlayer = 0;
        }

        private void ChoosButton2_Click(object sender, RoutedEventArgs e)
        {
            label.Content = "kaufmänische Ausbildung:\n - ";

            setting.SelectedPlayer = 1;
        }

        private void ChoosButton3_Click(object sender, RoutedEventArgs e)
        { 
            label.Content = "duale Studium-Richtung";

            setting.SelectedPlayer = 2;
        }

        private void ChoosButton4_Click(object sender, RoutedEventArgs e)
        {
            label.Content = "Maschinenfabrik Reinhausen";

            setting.SelectedPlayer = 3;
        }

        private SettingDto ReadJason()
        {
            SettingDto result = new SettingDto();

            if (!File.Exists(path))
            {
                List<Player> players = new List<Player>();
                players.Add(new Player() { Name = "Einfachmacher", Imgpath = @"..\..\..\..\..\assets\images\player\einfachmacher.png", No = 0 });
                players.Add(new Player() { Name = "Kundenversteher", Imgpath = @"..\..\..\..\..\assets\images\player\Original\Kundenversteher.png", No = 1 });
                players.Add(new Player() { Name = "Vorangeher", Imgpath = @"..\..\..\..\..\assets\images\player\Original\vorangeher.png", No = 2 });
                players.Add(new Player() { Name = "Zusammenbringer", Imgpath = @"..\..\..\..\..\assets\images\player\Original\Zusammenbringer.png", No = 3 });
                result.Players = players.ToArray();
                result.SelectedPlayer = 1;

                string content = Serialize.ToJson(result);
                File.WriteAllText(path, content);
            }
            else
            {
                string jsoncontent = File.ReadAllText(path);
                result = SettingDto.FromJson(jsoncontent);
            }

            return result;
        }

        private void WriteJson()
        {
            string content = Serialize.ToJson(setting);
            File.WriteAllText(path, content);
        }
    }
}

