echo "Do you wish to setup a door alarm?"
select yn in "Yes" "No"; do
    case $yn in
        Yes ) crontab -l | { cat; echo "@reboot sleep 67 && sudo python /home/pi/freezeralarm/startupbeep.py"; } | crontab -

echo "Do you wish to enable singledooralarm or doubledooralarm?"
select yn in "SingleDoor" "DoubleDoor"; do
    case $yn in
        SingleDoor ) sudo cp /home/pi/freezeralarm/singledooralarm.service /etc/systemd/system; crontab -l | { cat; echo "@reboot sleep 60 && sudo systemctl restart singledooralarm.service
"; } | crontab -; sudo systemctl enable singledooralarm.service; echo "Enter Twilio SID"; read twiliosid; echo $twiliosid; sed -i "11s/account_sid.*/account_sid = '$twiliosid'/g" /home/pi/freezeralarm/singledooralarm.py; echo "Enter Twilio Token"; read twiliotoken; echo $twiliotoken; sed -i "12s/auth_token.*/auth_token = '$twiliotoken'/g" /home/pi/freezeralarm/singledooralarm.py; echo "Enter Twilio From Number example: 12223334444"; read twiliofrom; echo $twiliofrom; sed -i "10s/fromnumber.*/fromnumber = '+$twiliofrom'/g" /home/pi/freezeralarm/singledooralarm.py; echo "Enter Numbers to message example with single quotes, + and commas: '+12223334444', '+19998765432'"; read twiliomessages; echo $twiliomessages; sed -i "9s/numbers_to_message.*/numbers_to_message = [$twiliomessages]/g" /home/pi/freezeralarm/singledooralarm.py; break;;
        DoubleDoor ) sudo cp /home/pi/freezeralarm/doubledooralarm.service /etc/systemd/system; crontab -l | { cat; echo "@reboot sleep 60 && sudo systemctl restart doubledooralarm.service
"; } | crontab -; sudo systemctl enable doubledooralarm.service; echo "Enter Twilio SID"; read twiliosid; echo $twiliosid; sed -i "11s/account_sid.*/account_sid = '$twiliosid'/g" /home/pi/freezeralarm/doubledooralarm.py; echo "Enter Twilio Token"; read twiliotoken; echo $twiliotoken; sed -i "12s/auth_token.*/auth_token = '$twiliotoken'/g" /home/pi/freezeralarm/doubledooralarm.py; echo "Enter Twilio From Number example: 12223334444"; read twiliofrom; echo $twiliofrom; sed -i "10s/fromnumber.*/fromnumber = '+$twiliofrom'/g" /home/pi/freezeralarm/doubledooralarm.py; echo "Enter Numbers to message example with single quotes, + and commas: '+12223334444', '+19998765432'"; read twiliomessages; echo $twiliomessages; sed -i "9s/numbers_to_message.*/numbers_to_message = [$twiliomessages]/g" /home/pi/freezeralarm/doubledooralarm.py; break;;
    esac
done; break;;
        No ) break;;
    esac
done

echo "Do you wish to setup temperature alarms?"
select yn in "Yes" "No"; do
    case $yn in
        Yes ) echo "Enter temperature(F) threshold example 20 "; read temp; echo $temp; sed -i "25s/tempAlarmThreshold.*/tempAlarmThreshold = '$temp'/g" /home/pi/freezeralarm/tempalarm.py;!!!!!!! echo "Enter duration over threshold to trigger alarm threshold example 20 "; read time; echo $time; sed -i "26s/tempAlarmDuration.*/tempAlarmDuration = '$time'/g" /home/pi/freezeralarm/tempalarm.py; sudo cp /home/pi/freezeralarm/tempalarm.service /etc/systemd/system; sudo systemctl enable tempalarm.service;  echo "Did you just setup a freezer alarm?"
select yn in "Yes" "No"; do
    case $yn in
        Yes ) echo $twiliosid; sed -i "11s/account_sid.*/account_sid = '$twiliosid'/g" /home/pi/freezeralarm/tempalarm.py; echo $twiliotoken; sed -i "12s/auth_token.*/auth_token = '$twiliotoken'/g" /home/pi/freezeralarm/tempalarm.py; echo $twiliofrom; sed -i "10s/fromnumber.*/fromnumber = '+$twiliofrom'/g" /home/pi/freezeralarm/tempalarm.py; sed -i "9s/numbers_to_message.*/numbers_to_message = [$twiliomessages]/g" /home/pi/freezeralarm/tempalarm.py; echo "All entries copied over"; break;;
        No ) echo "Enter Twilio SID"; read twiliosid; echo $twiliosid; sed -i "11s/account_sid.*/account_sid = '$twiliosid'/g" /home/pi/freezeralarm/tempalarm.py; echo "Enter Twilio Token"; read twiliotoken; echo $twiliotoken; sed -i "12s/auth_token.*/auth_token = '$twiliotoken'/g" /home/pi/freezeralarm/tempalarm.py; echo "Enter Twilio From Number example: 12223334444"; read twiliofrom; echo $twiliofrom; sed -i "10s/fromnumber.*/fromnumber = '+$twiliofrom'/g" /home/pi/freezeralarm/tempalarm.py; echo "Enter Numbers to message example with single quotes, + and commas: '+12223334444', '+19998765432'"; read twiliomessages; echo $twiliomessages; sed -i "9s/numbers_to_message.*/numbers_to_message = [$twiliomessages]/g" /home/pi/freezeralarm/tempalarm.py;break;;
    esac
done;  break;;
        No ) break;;
    esac
done; 

echo "Do you wish to setup temperature monitoring?"
select yn in "Yes" "No"; do
    case $yn in
        Yes ) sudo cp /home/pi/freezeralarm/tempiodata.service /etc/systemd/system; sudo systemctl enable tempiodata.service; echo "Enter Adafruit IO key"; read iokey; echo $iokey; sed -i "7s/IO KEY/$iokey/g" /home/pi/freezeralarm/tempiodata.py; echo "Enter Adafruit username"; read username; echo $username; sed -i "8s/user name/$username/g" /home/pi/freezeralarm/tempiodata.py; break;;
        No ) exit;;
    esac
done; 
