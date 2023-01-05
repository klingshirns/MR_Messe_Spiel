using System.Collections.Generic;
using System.IO;
using System.Windows;

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

        //Einfachmacher
        private void Button_Click_6(object sender, RoutedEventArgs e)
        {
            label.Content = "Technische Ausbildung:\n";
            label2.Content = "- setzten auf 80 Prozent Lösungen und verbessern bei Bedarf\n- Lösungen klein und kompakt, kein Schnickschnack";
            label3.Content = "- eindeutige Prioritäten\n- denken und handeln ergebnisorientiert";

            setting.SelectedPlayer = 0;
        }

        //Kundenversteher
        private void ChoosButton2_Click(object sender, RoutedEventArgs e)
        {
            label.Content = "Duale Studium-Richtung";
            label2.Content = "- Bei Entscheidungen in Kunden hinein versetzen\n- Einsetzung für verlässliche und gewinnbringende Partnerschaften";
            label3.Content = "- genaues Hinhören bei Kunden\n- aktive Entwicklungen mit Kunden teilen\n- professionelles Auftreten bei internen und externen Kunden";

            setting.SelectedPlayer = 2;
        }

        //Vorangeher
        private void ChoosButton3_Click(object sender, RoutedEventArgs e)
        {
            label.Content = "Kaufmänische Ausbildung:\n";
            label2.Content = "- strategische Leitplanken\n- Engagement und Zuverlässigkeit bei neuen Themen\n- echter Kämpfer, der so schnell nichts aufhält\n- Mitziehung anderer durch Begeisterung";
            label3.Content = "- treffen schnelle Entscheidungen\n- unterstützen zielstrebige KollegInnen\n- setzen entschiedene Themen zielstrebig um";

            setting.SelectedPlayer = 1;
        }

        //Zusammenbringer
        private void ChoosButton4_Click(object sender, RoutedEventArgs e)
        {
            label.Content = "Maschinenfabrik Reinhausen";
            label2.Content = "- Informationen schnell und verständlich verteilen\n- gegenseitig einbringen passend zu unseren Kompetenzen und Fähigkeiten\n- Feedback bei fehlende Zusammenarbeit und suchen gemeinsame Lösungen";
            label3.Content = "- Vertretung gemeinsamer getroffene Entscheidungen\n- Leistung anderer wertschätzen\n- vertrauenswürdige Ausstrahlung";

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
                players.Add(new Player() { Name = "Vorangeher", Imgpath = @"..\..\..\..\..\assets\images\player\Original\Vorangeher.png", No = 2 });
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

