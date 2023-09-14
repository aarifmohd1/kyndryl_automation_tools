# Images available in the Kyndryl Automation Lab

| Image name | OS | Subsystems | Available in DTL | Notes | Cloud providers |
|---|---|---|---|---|---|
| cos7-1 | CentOS Linux 7 | | Yes | Kyndryl compliant | Azure |
| cos8-1 | CentOS Linux 8 | | Yes | Kyndryl compliant | Azure |
| edu1 | Fedora 37 | libvirt (KVM), git, ansible, 5 VMs | No | Only manual access (public IP), dedicated for education lessons | Azure |
| rh61-1 | Red Hat Enterprise Linux 6.1 | | Yes | Kyndryl compliant | Azure |
| rh76-1 | Red Hat Enterprise Linux 7.6 | | Yes | Kyndryl compliant | Azure |
| rh77-1 | Red Hat Enterprise Linux 7.7 | | Yes | Kyndryl compliant | Azure |
| rh78-1 | Red Hat Enterprise Linux 7.8 | | Yes | Kyndryl compliant | Azure |
| rh79-1 | Red Hat Enterprise Linux 7.9 | | Yes | Kyndryl compliant | Azure |
| rh84-1 | Red Hat Enterprise Linux 8.4 | | Yes | Kyndryl compliant | Azure |
| rh84-2 | Red Hat Enterprise Linux 8.4 | DB2 | Yes | Kyndryl compliant | Azure |
| rh86-1 | Red Hat Enterprise Linux 8.6 | | Yes | Kyndryl compliant | Azure |
| rh86-2 | Red Hat Enterprise Linux 8.6 | Oracle DB | Yes | Kyndryl compliant | Azure |
| rh86-3 | Red Hat Enterprise Linux 8.6 | WAS | Yes | Kyndryl compliant | Azure |
| rh86-4 | Red Hat Enterprise Linux 8.6 | MQ | Yes | Kyndryl compliant | Azure |
| rh86-5 | Red Hat Enterprise Linux 8.6 | TWS | Yes | Kyndryl compliant | Azure |
| rh86-6 | Red Hat Enterprise Linux 8.6 | Nexus | Yes | Kyndryl compliant | Azure |
| rh91-1 | Red Hat Enterprise Linux 9.1 | | Yes | Kyndryl compliant | Azure |
| su12-1 | SUSE Linux Enterprise Server 12.5 | | Yes | Kyndryl compliant | Azure |
| su15-1 | SUSE Linux Enterprise Server 15 | | Yes | Kyndryl compliant | Azure |
| w2012-1 | MS Windows Server 2012R2 DC | | Yes | Kyndryl compliant | Azure |
| w2016-1 | MS Windows Server 2016 DC | | Yes | Kyndryl compliant | Azure |
| w2019-1 | MS Windows Server 2019 DC | | Yes | Kyndryl compliant | Azure |
| w2022-1 | MS Windows Server 2022 DC | | Yes | Kyndryl compliant | Azure |
| w2012-2 | MS Windows Server 2012R2 DC | IIS | Yes | Kyndryl compliant | Azure |
| w2016-2 | MS Windows Server 2016 DC | IIS | Yes | Kyndryl compliant | Azure |
| w2019-2 | MS Windows Server 2019 DC | IIS | Yes | Kyndryl compliant | Azure |
| w2022-2 | MS Windows Server 2022 DC | IIS, MSSQL, MySQL | Yes | Kyndryl compliant | Azure |
| w2022-3 | MS Windows Server 2022 DC | TSM | Yes | Kyndryl compliant | Azure |

Virtual machines created from these images in shared environment (DTL) are named `<Image name>-<Job ID>` so for example `w2019-1-123456`. Hostnames are identical with the image names. VMs are not allowed to exist more than 4 hours, longer running jobs will get connection error after this time, because the VMs will be removed automatically.
