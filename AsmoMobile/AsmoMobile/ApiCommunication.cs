using System;
using System.Collections.Generic;
using System.Net;
using System.Net.Http;
using System.Text;

namespace AsmoMobile
{
    class ApiCommunication
    {
        public static void setMotorSpeed(int speed, int direction)
        {
            int motor1speed = 0; //left wheels
            int motor2speed = 0; //right wheels
            if (direction < 0)
            {
                //drive left
                motor1speed = speed + (speed * (direction / 100)) * 2;
                motor2speed = speed;
            }
            else if (direction > 0)
            {
                //drive right
                motor1speed = speed;
                motor2speed = speed + (speed * ((-1 * direction) / 100) * 2);
            }
            else if (direction == 0)
            {
                //drive straight
                motor1speed = speed;
                motor2speed = speed;
            }
            WebClient clientAsmo = new WebClient();
            var reqparm = new System.Collections.Specialized.NameValueCollection();
            reqparm.Add("motor1", motor1speed.ToString());
            reqparm.Add("motor2", motor2speed.ToString());
            clientAsmo.UploadValues("http://localhost:8080/api/motor", "POST", reqparm);


        }
    }
}
