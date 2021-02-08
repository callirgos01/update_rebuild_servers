echo stopping radarr...
sudo systemctl stop radarr.service
echo into raddarr-source
cd /usenet/setup/Radarr/Radarr-source
echo git pull...
git pull
echo restore
dotnet restore /usenet/setup/Radarr/Radarr-source/src/Radarr.sln
echo building...
./build.sh
echo building done.
echo creating link...
ln -s /usenet/setup/Radarr/Radarr-source/_output/UI /usenet/setup/Radarr/Radarr-source/_output/net5.0/linux-x64/UI 
echo starting radarr again
sudo systemctl start radarr.service
