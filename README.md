# README

## Synopsis

_Short high level description. Max 5 sentences for high level understanding purpose of the asset. No technical details!_

## Variables

* _Describe **ALL variables** which consumer can use._
* _Describe (in the column "Comments") how the variable influents behaviour of the Ansible Role. In the case of complex/long description, put it into subchapter of the chapter **Procedure** and put link to mentioned subchapter_
* _Put variables in alphabetical order_
* _If it makes **STRONG sense** you can split list of variables to more tables._
* _To have clarity which variables are mandatory and which optional_
* _Show default value (if exists)_
* _Show expected units  (kB, MB, seconds, ….)_
* _Show simplified types (String, Number, Integer, Boolean, Array, Dictionary)_
  * _In case of Enumerated type - describe all accepted options and their meaning in the column "Comments"_
  * _In case of structured variable (Array, Dictionaty) create separate `README_variable_name.md` with description meaning of the structure and examples of structured values. THis file must be linked from "Comment" column_

Variable | Default| Comments
----------|-----------------|--------
**variable1** (type) | default value| **Mandatory** Description of the variable
**variable2** (type) | default value| Description of the variable
**variable3** (type) | default value| Description of the variable
... | ... |  ...

## Results from execution

_List and description of all states (represented by unique Return Codes) where Ansible Role can finish of its execution._
_See documentation for [Return Code](https://github.kyndryl.net/Continuous-Engineering/ansible_role_returncode/) Building Block_

Return Code Group | Return Code | Comments
----------|--------------|---------
String value set to variable `rc_group` | Integer value set to variable `rc_number` |  Description of meaning of given return code
String value set to variable `rc_group` | Integer value set to variable `rc_number` |  Description of meaning of given return code
... | ... |  ...

## Procedure

_Detailed description what automaton does._
_If needed to create subchapters for description meaning of specific "complex" variables_

## Support

_Information how to submit issue, what is a governance, who are main contacts, what is email task ID or Slack Channel for communication, ..._
_If some information are common for more assets at once - maintain them centrally and put here link_
_Generally see [12 factors to measuring an open source project's health](https://www.redhat.com/en/blog/12-factors-measuring-open-source-projects-health) following sections from the document should be reflected in this chapter:_

* _Project life cycle_
* _Governance_
* _Project leads_
* _Goals and roadmap_
* _Onboarding processes_
* _Outreach_

## Deployment

* _In the case of Ansible Collection - detailed description how the asset should be deployed into "framework":_
  * _How to configure Ansible Tower Project and Job Template. Instructions **must be in accordance of [CACF Ansible Tower Object Naming Standards](https://github.kyndryl.net/Continuous-Engineering/TWPs/tree/master/CACF%20Ansible%20Tower%20Object%20Naming%20Standards)!**_
* _In the case of Ansible Role which is plugable to specific Ansible Framework - this chapter must contain link to General Deployment Instructions for given Framework. For example:_
  * _[Deployment Instructions for CACF Event Automation](https://continuous-engineering.eu-de.mybluemix.net/markdown/Continuous-Engineering%2FCACM_Automation_Services%2Fhowto-deploy-new-ansible-automation.md)_
  * _[Deployment Instructions for CACF Service Request Automation](https://github.kyndryl.net/Continuous-Engineering/CE-Documentation/tree/master/Community%20Guidelines/Ansible%20Guides/SRA%20Guides)_
* _In the case of Ansible Role which is intended for specific Ansible Collection only, this chapter must contain link to this Collection._
* _In the case of Ansible Role is Generic Reusable "component" and can be used in whatever another Ansible Collections - this chapter must contain reference to chapter [Examples](#examples) where must be commented pieces of code which demonstrate how to incorporate Ansible Role to another solution. Typical examples of Generic Reusable "component" are [Building Blocks](https://github.kyndryl.net/Continuous-Engineering/CE-Documentation/blob/master/Community%20Guidelines/Ansible%20Guides/Development%20Standards/BuildingBlocks.md)._

## Known problems and limitations

* _Description of all limitations and known problems._
  * _Which platforms are or are not supported_
* _..._

## Prerequisites

* _Description of environment and prerequisites which are needed for correct functionality of the Ansible Role._

## Examples

* _Example how to use Ansible Role in a Playbook_

## License

[Kyndryl Intellectual Property](https://github.kyndryl.net/Continuous-Engineering/CE-Documentation/blob/master/files/LICENSE.md)
