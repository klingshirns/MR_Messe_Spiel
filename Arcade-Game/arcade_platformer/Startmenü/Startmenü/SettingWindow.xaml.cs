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
        private readonly string filename = @"..\..\..\..\json\player.json";

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
            EinfachmacherLabel.Foreground = System.Windows.Media.Brushes.Red;
            KundenversteherLabel.Foreground = (System.Windows.Media.SolidColorBrush)new System.Windows.Media.BrushConverter().ConvertFrom("#FFDDDDDD");
            VorangeherLabel.Foreground = (System.Windows.Media.SolidColorBrush)new System.Windows.Media.BrushConverter().ConvertFrom("#FFDDDDDD");
            ZusammenbringerLabel.Foreground = (System.Windows.Media.SolidColorBrush)new System.Windows.Media.BrushConverter().ConvertFrom("#FFDDDDDD");

            label.Content = "Technische Ausbildung:\n";
            label2.Content = "- setzten auf 80 Prozent Lösungen und verbessern bei Bedarf\n- Lösungen klein und kompakt, kein Schnickschnack";
            label3.Content = "- eindeutige Prioritäten\n- denken und handeln ergebnisorientiert";

            setting.SelectedPlayer = 0;
        }

        //Kundenversteher
        private void ChoosButton2_Click(object sender, RoutedEventArgs e)
        {
            EinfachmacherLabel.Foreground = (System.Windows.Media.SolidColorBrush)new System.Windows.Media.BrushConverter().ConvertFrom("#FFDDDDDD");
            KundenversteherLabel.Foreground = System.Windows.Media.Brushes.Red;
            VorangeherLabel.Foreground = (System.Windows.Media.SolidColorBrush)new System.Windows.Media.BrushConverter().ConvertFrom("#FFDDDDDD");
            ZusammenbringerLabel.Foreground = (System.Windows.Media.SolidColorBrush)new System.Windows.Media.BrushConverter().ConvertFrom("#FFDDDDDD");

            label.Content = "Duale Studium-Richtung";
            label2.Content = "- genaues Hinhören, hinein versetzen, aktive Entwicklungen teilen\n  und professionelles Auftreten bei internen und externen Kunden";
            label3.Content = "- Einsetzung für verlässliche und\n  gewinnbringende Partnerschaften";

            setting.SelectedPlayer = 2;
        }

        //Vorangeher
        private void ChoosButton3_Click(object sender, RoutedEventArgs e)
        {
            EinfachmacherLabel.Foreground = (System.Windows.Media.SolidColorBrush)new System.Windows.Media.BrushConverter().ConvertFrom("#FFDDDDDD");
            KundenversteherLabel.Foreground = (System.Windows.Media.SolidColorBrush)new System.Windows.Media.BrushConverter().ConvertFrom("#FFDDDDDD");
            VorangeherLabel.Foreground = System.Windows.Media.Brushes.Red;
            ZusammenbringerLabel.Foreground = (System.Windows.Media.SolidColorBrush)new System.Windows.Media.BrushConverter().ConvertFrom("#FFDDDDDD");

            label.Content = "Kaufmänische Ausbildung:\n";
            label2.Content = "- Engagement, Zuverlässigkeit und Zielstrebigkeit bei neuen Themen\n- unterstützen und Mitziehung zielstrebige KollegInnen durch Begeisterung";
            label3.Content = "- strategische Leitplanken\n- treffen schnelle Entscheidungen";

            setting.SelectedPlayer = 1;
        }

        //Zusammenbringer
        private void ChoosButton4_Click(object sender, RoutedEventArgs e)
        {
            EinfachmacherLabel.Foreground = (System.Windows.Media.SolidColorBrush)new System.Windows.Media.BrushConverter().ConvertFrom("#FFDDDDDD");
            KundenversteherLabel.Foreground = (System.Windows.Media.SolidColorBrush)new System.Windows.Media.BrushConverter().ConvertFrom("#FFDDDDDD");
            VorangeherLabel.Foreground = (System.Windows.Media.SolidColorBrush)new System.Windows.Media.BrushConverter().ConvertFrom("#FFDDDDDD");
            ZusammenbringerLabel.Foreground = System.Windows.Media.Brushes.Red;

            label.Content = "Maschinenfabrik Reinhausen";
            label2.Content = "- Feedback geben, gemeinsame Lösungssuche und vertrauenswürdige Ausstrahlung\n- Leistung anderer wertschätzen und Kompetenzen und Fähigkeiten passend einsetzen";
            label3.Content = "- Informationen schnell und verständlich verteilen\n- Vertretung gemeinsamer getroffene Entscheidungen";

            setting.SelectedPlayer = 3;
        }

        private SettingDto ReadJason()
        {
            SettingDto result = new SettingDto();

            if (!File.Exists(filename))
            {
                List<Player> players = new List<Player>();
                players.Add(new Player() { Name = "Einfachmacher", Imgpath = @"..\..\..\..\..\assets\images\player\einfachmacher.png", No = 0 });
                players.Add(new Player() { Name = "Kundenversteher", Imgpath = @"..\..\..\..\..\assets\images\player\Original\Kundenversteher.png", No = 1 });
                players.Add(new Player() { Name = "Vorangeher", Imgpath = @"..\..\..\..\..\assets\images\player\Original\Vorangeher.png", No = 2 });
                players.Add(new Player() { Name = "Zusammenbringer", Imgpath = @"..\..\..\..\..\assets\images\player\Original\Zusammenbringer.png", No = 3 });
                result.Players = players.ToArray();
                result.SelectedPlayer = 1;

                string content = Serialize.ToJson(result);
                File.WriteAllText(filename, content);
            }
            else
            {
                string jsoncontent = File.ReadAllText(filename);
                result = SettingDto.FromJson(jsoncontent);
            }

            return result;
        }

        private void WriteJson()
        {
            string content = Serialize.ToJson(setting);
            File.WriteAllText(filename, content);
        }
    }
}

