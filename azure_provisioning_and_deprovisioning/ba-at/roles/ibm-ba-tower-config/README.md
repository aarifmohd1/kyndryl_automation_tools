ibm-ba-tower-config
===================

This role contains the task used to configure Ansible Tower thorugh Ansible playbooks using AT API. These task can be used whenever someone require to configure a component on AT for e.g Adding host to inventory, creating job template, Launching job template etc.

** NOTE: _Don't call this role directly , import the tasks from this role whenever required_

The role contains the below given task:-

1. Add a group to Inventory
2. Add a host to Inventory
3. Add multiple hosts to a group
4. Attach Instance Group
5. Configure a Template
6. Create different type of Credentials
7. Create Inventory
8. Create Job Template
9. Create organisation
10. Create Project
11. Query for a credential
12. Query for a Group
13. Query for an Inventory
14. Query for a Job Template
15. Query for a Organisation
16. Query for a Project
17. Ping Tower


Requirements
------------

1. Since this role contains the tasks for AT configuration so there must be a running ansible tower setup to work with this role.
2. Privileged AT credentials to work with Ansible Tower API.

Variables
----------

Each of the tasks file inside this role has different different variable requiremnets. One needs to supply variable as per the task being imported.

Below are all the variables used inside the tasks of this role.

| Variables | Default Value | Comments |
| --------- | ------------- | -------- |
cred_name | - | Name of the credential to be created
cred_type ( along with other credential related variables as per the type ) | - | Type of the credential to be created
enable_survey | - | Whether to enable the survey or not ( "yes" or "no)
group_name | - | Name of the group to Query or create
group_description | - | Description of the group to be created
group_id | - | Group ID ( required while adding host/hosts to a group)
host_name_or_ip | - | Hostname/IP ( required while adding hosts to an inventory or group)
inventory_name | - | Name of the inventory to query or create
inv_id | - | Inventory ID (required while adding hosts to an inventory or querying a group inside an inventory)
job_extra_vars | - | Extra vars for a job template
job_template_name | - | Name of the job template to query or create
list_of_hosts | - | Hosts list to be added to a group 
login_password  | - | Ansible Tower Login password to work with tower API
login_user | - | Ansible Tower Login user(privileged) to work with tower API 
org_id | - | Organization ID to query for templates, projects, inventory, credentials etc.
org_name | - | Name of the organization to query or create
org_desc | - | Description of the organization while creating an organization
project_id | - | Project ID ( Required while creating a job template to attach the project)
playbook_name | - | Name of the playbook ( Required while creating a job template to attach the playbook)
project_name | - | Name of the project to query or create
tower_ip | - |  Ansible Tower IP to work with tower API

Example 
--------

- Including an example of how to import this role and use a task inside your playbook
    <pre><code>
    name: query inventory {{ inventoryName }}
    import_role:
        name: ba-at
        tasks_from: get_inventory
    vars:
      inventory_name: "{{ inventoryName }}"
      tower_ip: "{{ lookup('env', 'TOWER_HOST') }}"
      login_user: "{{ lookup('env', 'TOWER_USERNAME') }}"
      login_password: "{{ lookup('env', 'TOWER_PASSWORD') }}"
      org_id: "{{ org_id }}"
      </code></pre>


Support
-------

### Contact persons :
1. Arumugam Sakthimurugan - Sakthimurugan.Arumugam@kyndryl.com
2. BALASUBRAMANIAN MANIVASAGAM - bmanivas@kyndryl.com  
3. Shubham Kumar - shubham.kumar4@kyndryl.com  
4. Abhishek Chourasia - Abhishek.Chourasia@kyndryl.com


License
-------

[Kyndryl Intellectual Property](https://github.kyndryl.net/Continuous-Engineering/CE-Documentation/blob/master/files/LICENSE.md)

