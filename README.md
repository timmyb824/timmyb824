<h1 align="left">Hi 👋, I'm Tim Bryant</h1>
<h3 align="left">Passionate about Observability, Site Reliability, DevOps, and Automation</h3>

- 🌱 I’m currently working on [PEZ-ServerMonitor](https://github.com/timmyb824/PEZ-ServerMonitor)
 
- 📝 I sometimes write articles on [My Blog](https://blog.timothybryantjr.com)

- 🌐 Website [🖥️ Official](https://timothybryantjr.com)

- ⚡ Hobbies **learning new things, breaking and fixing things in my home-lab, watching sports, car detailing, working on my yard**

<h3 align="left">Homelab:</h3>

I run a small yet exciting home-lab within my house, where I constantly experiment and gain valuable knowledge. Here's a list of the equipment I currently have in my home-lab:

- **Dell Optiplex 5000 PC**: running Proxmox VE which hosts my k3s cluster
- **Two Beelink Mini PCs**:
  1. running Proxmox VE
  2. running several [podman](https://podman.io/) containers including my primary adguard-home for local dns
- **RasberryPI3**: runs replica adguard-home and acts as [qdevice](https://blog.jenningsga.com/proxmox-keeping-quorum-with-qdevices/) to ensure Proxmox HA
- **Synology NAS** (DS923+): for file storage
- **eero6 router & mesh network**
- **TP-Link un-managed gig switch**
- **APC UPS Pro 1500VA**: for power protection

Within my home lab, I operate multiple open-source applications, tools, and services. The majority of these are deployed within my k3s cluster, although some are deployed using docker/podman or directly on the VMs. For example, I utilize podman for deploying and backing up my adguardhome instances, whereas my PostgreSQL database and Zabbix monitoring server are directly deployed on the VMs. It is worth noting a few additional details:

- I employ [traefik](https://traefik.io/) as my reverse proxy for all components, including Kubernetes.
- To access my home lab from anywhere, I rely on [tailscale](https://tailscale.com/) (highly recommended) as my VPN solution.
- I manage my docker containers using [portainer](https://www.portainer.io/), while [Lens](https://k8slens.dev/) helps me manage my k3s cluster. Although I enjoy working with the terminal, I find GUIs useful for certain management tasks.
- [argocd](https://argoproj.github.io/cd/) serves as my gitops tool within the k3s cluster. Currently, approximately half of my services are deployed using argocd. However, I am cautious about relying entirely on argocd due to its potential impact on the cluster's performance.
- To handle secrets, I utilize [vault](https://developer.hashicorp.com/vault) and the [argocd-vault-plugin](https://github.com/argoproj-labs/argocd-vault-plugin) to inject secrets into pods as part of my gitops workflow. While I plan to transition all my secrets management to vault in the future, I have recently started using it. For other secrets, I directly inject them into manifests and docker-compose files using the command line tool `envsubst`.
- For monitoring, I employ a combination of tools such as [prometheus](https://prometheus.io/), [grafana](https://grafana.com/), and [alertmanager](https://prometheus.io/docs/alerting/latest/alertmanager/) through the [kube-prometheus-stack](https://github.com/prometheus-community/helm-charts/tree/main/charts/kube-prometheus-stack). Additionally, I utilize [zabbix](https://www.zabbix.com/) to monitor my network and VMs. Lastly, I rely on [uptime-kuma](https://github.com/louislam/uptime-kuma) to monitor the availability of my websites, services, and hosts.
- To handle local DNS, I rely on [adguardhome](https://github.com/AdguardTeam/AdGuardHome), and for ad-blocking, I combine adguardhome with [cloudflare](https://www.cloudflare.com/).

Apart from my home-lab, I have deployed multiple servers within Oracle Cloud Infrastructure (OCI) to host various services. This includes my [IP challenge website](https://github.com/timmyb824/ip-addr-challenge), which can be accessed at [ip-addr.timmybtech.com](https://ip-addr.timmybtech.com/), as well as a server running [Monika](https://monika.hyperjump.tech/), a command-line application for monitoring apps and services. By utilizing OCI, I ensure uninterrupted monitoring coverage that operates independently from my home-lab, offering reliability and resilience regardless of the status of my local infrastructure.

Finally, here is a screenshot showing a list of all the applications that are currently deployed in my home-lab:

<img src="homelab_updated.png"  width="600" height="300">


If you wish to delve deeper into my home-lab's operations, I have GitHub repositories housing the manifests, docker-compose files, and scripts that facilitate all my deployments. You can locate them here:

- **[configs](https://github.com/timmyb824/configs)**
- **[automations](https://github.com/timmyb824/automations)**
- **[docker-apps](https://github.com/timmyb824/docker-apps)**
- **[kubernetes-apps](https://github.com/timmyb824/kubernetes-apps)**

<h3 align="left">Connect with me:</h3>
<p align="left">
<a href="https://twitter.com/timmyb824" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/twitter.svg" alt="timmyb824" height="30" width="40" /></a>
<a href="https://linkedin.com/in/timothy-bryant-7aa00026" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/linked-in-alt.svg" alt="timothy-bryant-7aa00026" height="30" width="40" /></a>
</p>

<h3 align="left">Stats:</h3>

<p>&nbsp;<img align="center" src="https://github-readme-stats.vercel.app/api?username=timmyb824&show_icons=true&locale=en&theme=tokyonight" alt="timmyb824" /></p>

<img align="center" src="/github-metrics.svg" alt="Metrics" width="400">

<a href="https://app.daily.dev/DailyDevTips"><img src="https://github.com/timmyb824/timmyb824/blob/main/devcard.svg" width="400" alt="Tim Bryant's Dev Card"/></a>
