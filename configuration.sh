echo "Do you wish to enable singledooralarm.service?"
select yn in "Yes" "No"; do
    case $yn in
        Yes ) sudo cp /home/pi/freezeralarm/singledooralarm.service /etc/systemd/system; crontab -l | { cat; echo "@reboot sleep 45 && sudo systemctl restart singledooralarm.service
"; } | crontab -; sudo systemctl enable singledooralarm.service; echo "Enter Twilio SID"; read twiliosid; echo $twiliosid; sed -i "11s/account_sid.*/account_sid = '$twiliosid'/g" /home/pi/freezeralarm/singledooralarm.py; echo "Enter Twilio Token"; read twiliotoken; echo $twiliotoken; sed -i "12s/auth_token.*/auth_token = '$twiliotoken'/g" /home/pi/freezeralarm/singledooralarm.py; echo "Enter Twilio From Number example: 12223334444"; read twiliofrom; echo $twiliofrom; sed -i "10s/fromnumber.*/fromnumber = '+$twiliofrom'/g" /home/pi/freezeralarm/singledooralarm.py; echo "Enter Numbers to message example with single quotes, + and commas: '+12223334444', '+19998765432'"; read twiliomessages; echo $twiliomessages; sed -i "9s/numbers_to_message.*/numbers_to_message = [$twiliomessages]/g" /home/pi/freezeralarm/singledooralarm.py;
 break;;
        No ) break;;
    esac
done

echo "Do you wish to enable doubledooralarm.service?"
select yn in "Yes" "No"; do
    case $yn in
        Yes ) sudo cp /home/pi/freezeralarm/doubledooralarm.service /etc/systemd/system; crontab -l | { cat; echo "@reboot sleep 45 && sudo systemctl restart doubledooralarm.$
"; } | crontab -; sudo systemctl enable doubledooralarm.service; sudo systemctl enable singledooralarm.service; echo "Enter Twilio SID"; read twiliosid; echo $twiliosid; sed -i "11s/account_sid.*/account_sid = '$twiliosid'/g" /home/pi/freezeralarm/singledooralarm.py; echo "Enter Twilio Token"; read twiliotoken; echo $twiliotoken; sed -i "12s/auth_token.*/auth_token = '$twiliotoken'/g" /home/pi/freezeralarm/singledooralarm.py; echo "Enter Twilio From Number example: 12223334444"; read twiliofrom; echo $twiliofrom; sed -i "10s/fromnumber.*/fromnumber = '+$twiliofrom'/g" /home/pi/freezeralarm/singledooralarm.py; echo "Enter Numbers to message example with single quotes, + and commas: '+12223334444', '+19998765432'"; read twiliomessages; echo $twiliomessages; sed -i "9s/numbers_to_message.*/numbers_to_message = [$twiliomessages]/g" /home/pi/freezeralarm/singledooralarm.py; break;;
        No ) break;;
    esac
done

echo "Do you wish to enable tempiodata.service?"
select yn in "Yes" "No"; do
    case $yn in
        Yes ) sudo cp /home/pi/freezeralarm/tempiodata.service /etc/systemd/system; sudo systemctl enable tempiodata.service; echo "Enter Adafruit IO key"; read iokey; echo $iokey; sed -i "7s/IO KEY/$iokey/g" /home/pi/freezeralarm/tempiodata.py; echo "Enter Adafruit username"; read username; echo $username; sed -i "8s/user name/$username/g" /home/pi/freezeralarm/tempiodata.py; break;;
        No ) exit;;
    esac
done
