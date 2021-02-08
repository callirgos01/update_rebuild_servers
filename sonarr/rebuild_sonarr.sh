echo stopping sonarr...
sudo systemctl stop sonarr.service
echo into sonarr-source
cd /usenet/setup/Sonarr/Sonarr-Source
rm -rf /usenet/setup/Sonarr/Sonarr-Source/_*
echo git pull...
git pull
echo relinking...
dotnet restore /usenet/setup/Sonarr/Sonarr-Source/src/Sonarr.sln
echo building...
./build.sh
echo building done.
echo starting sonarr again
sudo systemctl start sonarr.service
