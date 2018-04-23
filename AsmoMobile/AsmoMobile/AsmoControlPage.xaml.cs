using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

using Xamarin.Forms;
using Xamarin.Forms.Xaml;

namespace AsmoMobile
{
	[XamlCompilation(XamlCompilationOptions.Compile)]
	public partial class AsmoControlPage : ContentPage
	{
		public AsmoControlPage ()
		{
			InitializeComponent ();
            webv_camera.Source = "http://" + App._hostAsmo + ":" + App._portAsmo + "/api/camera/Stream";

        }
        void sliSpeedValueChanged(object sender, ValueChangedEventArgs args)
        {
            //lbl_speed.Text = args.NewValue.ToString();
            ApiCommunication.setMotorSpeed((int)args.NewValue, (int)sliDirection.Value);
        }
        void sliDirectionValueChanged(object sender, ValueChangedEventArgs args)
        {
            //lbl_direction.Text = args.NewValue.ToString();
            ApiCommunication.setMotorSpeed((int)sliSpeed.Value, (int)args.NewValue);
        }
    }
}