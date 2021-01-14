using System;
using System.Collections.Generic;
using System.Globalization;
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
using System.Windows.Navigation;
using System.Windows.Shapes;

namespace Soib_dotnet
{
    /// <summary>
    /// Interaction logic for MainWindow.xaml
    /// </summary>
    public partial class MainWindow : Window
    {
        public MainWindow()
        {
            InitializeComponent();
        }

        private void Calc_ber_button_Click(object sender, RoutedEventArgs e)
        {
            if (!double.TryParse(Mer_textbox.Text, out double mer))
            {
                MessageBox.Show("Wartość MER musi być liczbą.");
                return;
            }

            if(!int.TryParse(QamOrder_textbox.Text, out int qamOrder))
            {
                MessageBox.Show("Wartość QAM musi być liczbą.");
                return;
            }

            if (qamOrder != 4 && qamOrder != 16 && qamOrder != 64 && qamOrder != 128 && qamOrder != 256)
            {
                MessageBox.Show("Wartość QAM musi być potęgą liczby 2.");
                return;
            }
                
            ErrorWarning_Textblock.Visibility = Visibility.Hidden;    
            var calc = new Calc();
            var outputDict = calc.CalcBER(mer, qamOrder);
            Ber_result_textblock.Text = outputDict["ber"].ToString("#.##E+0");
            Error_textblock.Text = outputDict["error"].ToString("#.##E+0");

            if(outputDict["ber"] < outputDict["error"])
                ErrorWarning_Textblock.Visibility = Visibility.Visible;
        }

        private void Plot_button_Click(object sender, RoutedEventArgs e)
        {
            var calc = new Calc();
            calc.MakePlots();
        }
    }
}
