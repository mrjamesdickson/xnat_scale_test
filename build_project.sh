# simulate a large working XNAT instance
#1 create a project.
#2 populate with 100,000 sessions created from randomized dicom data. 
#3 create 500 users and assign to thet project
#4 add 100 container and asign to this project


URL='http://demo.xnatworks.io'
PROJECT='TEST123_PART1'
USERNAME='########'
PASSWORD='########'
DICOM='one/1.3.6.1.4.1.14519.5.2.1.1120973899807937478669042506932294829884-2-115-19brxp4.dcm'
IPADDRESS='192.168.1.64'
PORT='8104'



python3 xnat_create_project.py --xnat-url ${URL} --username ${USERNAME} --password ${PASSWORD} --project-id ${PROJECT} --project-name ${PROJECT} --project-description ${PROJECT}
python3 xnat_randomize_dicom.py ${DICOM} ${PROJECT} ${PROJECT}

dcmsend  ${IPADDRESS} ${PORT}  +r -aec XNAT --scan-directories ./${PROJECT}/1*.dcm +v -v
dcmsend  ${IPADDRESS}  ${PORT}  +r -aec XNAT --scan-directories ./${PROJECT}/2*.dcm +v -v
dcmsend  ${IPADDRESS}  ${PORT}  +r -aec XNAT --scan-directories ./${PROJECT}/3*.dcm +v -v
dcmsend  ${IPADDRESS}  ${PORT}  +r -aec XNAT --scan-directories ./${PROJECT}/4*.dcm +v -v
dcmsend  ${IPADDRESS}  ${PORT}  +r -aec XNAT --scan-directories ./${PROJECT}/5*.dcm +v -v
dcmsend  ${IPADDRESS}  ${PORT}  +r -aec XNAT --scan-directories ./${PROJECT}/6*.dcm +v -v
dcmsend  ${IPADDRESS}  ${PORT}  +r -aec XNAT --scan-directories ./${PROJECT}/7*.dcm +v -v
dcmsend  ${IPADDRESS}  ${PORT}  +r -aec XNAT --scan-directories ./${PROJECT}/8*.dcm +v -v
dcmsend  ${IPADDRESS}  ${PORT}  +r -aec XNAT --scan-directories ./${PROJECT}/9*.dcm +v -v



python xnat_generate_users.py --url ${URL} --username ${USERNAME} --password ${PASSWORD} --project ${PROJECT}
