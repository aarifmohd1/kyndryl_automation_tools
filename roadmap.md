# Roadmap

<table style="width:100%">
<tr>
<th style="width:10%"> Phase </th>
<th style="width:20%"> Objective </th>
<th style="width:40%"> Features </th>
<th style="width:30%"> Deliverables </th>
</tr>
<tr>
    <td> 1 </br>(delivered)</td>
<td> Shared Ansible environment initial release </td><td> <ul><li>Tower organization</li><li>Automatic Tower access</li><li>Connection to Azure</li><li>Connectivity to MCDS image gallery</li><li>Kyndryl compatible VMs with clean OSs</li><li>Playbooks execution on Azure VMs</li><li>Automatic VM provisioning</li><li>Automatic spin up/down</li><li>Automatic project creation</li><li>Automatic VM restoration after test</li></ul>
</td><td> SREs and system/subsystem SMEs who are supporting accounts will be able to start using the shared test environment to develop and test Ansible playbooks. They will be able to develop, configure, test, and showcase their automation capabilities.</td>
</tr>

<tr>
    <td> 2 </br>(delivered)</td>
    <td> Shared Ansible environment enhancement</td>
    <td> <ul><li>Parallel execution</li><li>More golden images</li><li>First component of middleware installation</li><li>Tower organization for management playbooks (VM provisiong, etc.)</li></td>
    <td> Expanding functionality of shared environment to be suitable for broader user base. </td>
</tr>
<tr>
    <td> 3 </br>(in progress)</td>
    <td> Shared Ansible environment integration</td>
    <td> <ul><li>More middleware installations</li><li>Documentation and examples of middlewares usage</li><li>Single point entry (one task that will do all testing steps - create project, create job template and execute)</li><li>Initial I-AIOps integration (presenting lab statistics data)</li><li>SFS enablement</li><li>Service IDs</li></ul></td>
    <td> Enhancing middleware capabilities of the Lab and enabling SFS uploads. Mandatory steps needed for GitOps. Migration to service IDs for standard operations. OneLAB integration with I-AIOps (oneLAB represented as individual account).
 </td>
</tr>
<tr>
    <td> 4 </br>(in planning)</td>
    <td> More middlewares in Shared lab</td>
    <td> <ul><li>More middlewares</li></ul></td>
    <td> Providing more and more middlewares.</td>
</tr>
</table>

## Planned features

- Advanced SNOW integration
  - Using SNOW tickets instead of usage of Tower (no more access to Tower)
  - All testing tasks performed exclusively from SNOW
  - Ticket based execution of playbook and return of Job log
- ACME customer
  - Creation of production-like team
  - Creation of processes
  - Dedicated MOM instance Tower organization
  - Dedicated Azure Subscription
  - MOM to Azure connection
  - Installation of OSs
  - Installation of Middleware
  - Creation of test data
