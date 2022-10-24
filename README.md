# Demystifying Ansible Automation Platform

<a href="https://www.packtpub.com/product/demystifying-ansible-automation-platform/9781803244884?utm_source=github&utm_medium=repository&utm_campaign=9781803244884"><img src="https://static.packt-cdn.com/products/9781803244884/cover/smaller" alt="About the Author" height="256px" align="right"></a>

This is the code repository for [Demystifying Ansible Automation Platform](https://www.packtpub.com/product/demystifying-ansible-automation-platform/9781803244884?utm_source=github&utm_medium=repository&utm_campaign=9781803244884), published by Packt.

**A definitive way to manage Ansible Automation Platform and Ansible Tower**

## What is this book about?
While you can use any automation software to simplify task automation, scaling automation to suit your growing business needs becomes difficult using only a command-line tool. Ansible Automation Platform standardizes how automation is deployed, initiated, delegated, and audited, and this comprehensive guide shows you how you can simplify and scale its management. 

This book covers the following exciting features:
* Get the hang of different parts of Ansible Automation Platform and their maintenance
* Back up and restore an installation of Ansible Automation Platform
* Launch and configure basic and advanced workflows and jobs
* Create your own execution environment using CI/CD pipelines
* Interact with Git, Red Hat Authentication Server, and logging services
* Integrate the Automation controller with services catalog
* Use Automation Mesh to scale Automation Controller

If you feel this book is for you, get your [copy](https://www.amazon.com/dp/1803244887) today!

## Chapters

|#|Chapter Name|Description|
|:---|:---|:---|
|1|Introduction to Ansible Automation Platform|Introduction to the book. The code in this chapter has examples of various code used in the book.|
|2|Installation of Ansible Automation Platform|Installation of the AAP on servers.|
|3|Installation of Ansible Automation Platform on OpenShift|Installation of the AAP with operators on OpenShift.|
|4|Configuring Settings and Authentication|Configuring settings and authentication the AAP|
|5|Configuring the Basics after Installation|Basics of creating organizations, credential types and credentials, and exporting configuration from the Automation Controller.|
|6|Configuring Role- Based Access Control|Configuring RBAC settings for the Automation controller and hub.|
|7|Inventories|Inventory and inventory source creation, including inventory plugin creation.|
|8|Creating Execution Environments|Execution Environment creation, as well as using configuration as code to create EEs|
|9|Automation Hub Management |Automation hub management including images, collections, and repositories.|
|10|Creating Job Templates and Workflows|Creation of projects, job templates, and workflows.|
|11|Creating Advanced Workflows and Jobs|Additional ways to use workflows and notifications.|
|12|Using CI/CD to interact with Automation controller|Using CI/CD and webhook specific playbooks, backup and restore, and ad hoc commands.|
|13|Integration with other services|Integration with other services, such as Red Hat insights, Splunk, and Prometheus.|
|14|Automate at scale with Automation Mesh|Automate at scale with Automation Mesh.|
|15|Using Ansible Services Catalog|Using Ansible Services Catalog.|




<a href="https://www.packtpub.com/?utm_source=github&utm_medium=banner&utm_campaign=GitHubBanner"><img src="https://raw.githubusercontent.com/PacktPublishing/GitHub/master/GitHub.png" 
alt="https://www.packtpub.com/" border="5" /></a>

## Instructions and Navigations
All of the code is organized into folders. For example, ch01.

The code will look like the following:
```
workflow_nodes:
  - identifier: Inventory Update
    related:
    unified_job_template:
    all_parents_must_converge: false
    extra_data: {}
```

**Following is what you need for this book:**
	This book is for IT administrators, DevOps engineers, cloud engineers, and automation engineers seeking to understand and maintain the controller part of Ansible Automation Platform. If you have basic knowledge of Ansible, can set up a virtual machine, or have OpenShift experience, and want to know more about scaling Ansible, this book is for you.

With the following software and hardware list you can run all code files present in the book (Chapter 1-15).
### Software and Hardware List
| Chapter | Software required | OS required |
| -------- | ------------------------------------ | ----------------------------------- |
| 1-15 | Ansible 2.13 | Windows, Mac OS X, and Linux (Any) |
| 1-15 | Python3 | Windows, Mac OS X, and Linux (Any) |
| 1-15 | Docker/Podman | Windows, Mac OS X, and Linux (Any) |
| 1-15 | Ansible Automation Platform 2.2 | Windows, Mac OS X, and Linux (Any) |

We also provide a PDF file that has color images of the screenshots/diagrams used in this book. [Click here to download it](https://packt.link/USfpC).

### Related products
* Practical Ansible 2 [[Packt]](https://www.packtpub.com/product/practical-ansible-2/9781789807462?_ga=2.219342297.1561952797.1663057129-1642543356.1635482889&utm_source=github&utm_medium=repository&utm_campaign=9781789807462) [[Amazon]](https://www.amazon.com/dp/1789807468)

* Mastering Ansible - Fourth Edition [[Packt]](https://www.packtpub.com/product/mastering-ansible/9781801818780?_ga=2.242811074.1561952797.1663057129-1642543356.1635482889&utm_source=github&utm_medium=repository&utm_campaign=9781801818780) [[Amazon]](https://www.amazon.com/dp/1801818789)

## Get to Know the Author
**Sean Sullivan**
works as a consultant for Red Hat and attended Purdue University, where he focused on networking. He has helped both small and large companies manage their Ansible deployments for the past five years, specializing in configuration as code and Ansible Automation Platform. He is a keen contributor to Red Hat’s GitHub repository and an avid board gamer whose favorite game is Brass: Birmingham.

### Download a free PDF

 <i>If you have already purchased a print or Kindle version of this book, you can get a DRM-free PDF version at no cost.<br>Simply click on the link to claim your free PDF.</i>
<p align="center"> <a href="https://packt.link/free-ebook/9781803244884">https://packt.link/free-ebook/9781803244884 </a> </p>