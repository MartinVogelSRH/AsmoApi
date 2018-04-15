using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Xamarin.Forms;

namespace AsmoMobile
{
	public partial class MainPage : ContentPage
	{
		public MainPage()
		{
			InitializeComponent();
		}
        void sliSpeedValueChanged(object sender, ValueChangedEventArgs args)
        {
            lbl_speed.Text = args.NewValue.ToString();
            ApiCommunication.setMotorSpeed((int)args.NewValue, (int)sliDirection.Value);
        }
        void sliDirectionValueChanged(object sender, ValueChangedEventArgs args)
        {
            lbl_direction.Text = args.NewValue.ToString();
            ApiCommunication.setMotorSpeed((int)sliSpeed.Value, (int)args.NewValue);
        }
    }
}
