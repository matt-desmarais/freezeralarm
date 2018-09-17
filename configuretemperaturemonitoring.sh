echo "Do you wish to enable tempiodata.service?"
select yn in "Yes" "No"; do
    case $yn in
        Yes ) sudo cp /home/pi/freezeralarm/tempiodata.service /etc/systemd/system; sudo systemctl enable tempiodata.service; echo "Enter Adafruit IO key"; read iokey; echo $iokey; sed -i "7s/IO KEY/$iokey/g" /home/pi/freezeralarm/tempiodata.py; echo "Enter Adafruit username"; read username; echo $username; sed -i "8s/user name/$username/g" /home/pi/freezeralarm/tempiodata.py; break;;
        No ) exit;;
    esac
done
