echo stopping lidarr...
sudo systemctl stop lidarr.service
echo into lidarr-source
cd /usenet/setup/Lidarr/Lidarr-Source
echo cleaning
rm -rf /usenet/setup/Lidarr/Lidarr-Source/_*
echo git pull...
git pull
# echo restore
 dotnet restore /usenet/setup/Lidarr/Lidarr-Source/src/Lidarr.sln --runtime linux-x64
echo building...
/usenet/setup/Lidarr/Lidarr-Source/build.sh
echo building done.
echo creating link...
ln -s /usenet/setup/Lidarr/Lidarr-Source/_output/UI /usenet/setup/Lidarr/Lidarr-Source/_output/netcoreapp3.1/linux-x64/UI
echo starting lidarr again
sudo systemctl start lidarr.service
