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
	public partial class SettingsPage : ContentPage
	{
		public SettingsPage()
		{
			InitializeComponent ();
            ent_Host.Text = App._hostAsmo;
            ent_Port.Text = App._portAsmo;
		}
        void btn_Save_OnClicked(object sender, EventArgs e)
        {
            App._hostAsmo = ent_Host.Text;
            App._portAsmo = ent_Port.Text;
            this.InvalidateMeasure();
        }
    }
}