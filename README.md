<h1 align="left">Hi 👋, I'm Tim Bryant</h1>
<h3 align="left">Passionate about Observability, Site Reliability, DevOps, and Automation</h3>

- 🌱 Check out my pins for projects I am currently working on or actively commit to

- 📝 I sometimes write articles on [My Blog](https://blog.timothybryantjr.com) (need to be better about this)

- 🌐 Website [🖥️ Official](https://timothybryantjr.com)

- ⚡ Hobbies **Learning new things, breaking and fixing things in my home-lab, watching sports, spending time with my family (Wife, Son, Dog, and 2 Cats)**

<h3 align="left">Homelab:</h3>

I run a small yet capable home-lab within my house, where I constantly experiment to gain new knowledge. Here's a list of the equipment I currently have in my home-lab:

- **Dell Optiplex 5000 PC**: running Proxmox VE which hosts my k3s cluster
- **Two Beelink Mini PCs**:
  1. running Proxmox VE (clustered with the Dell Optiplex 5000 PC)
  2. running several [podman](https://podman.io/) containers
- **RasberryPI3**: not currently used mainly due to its performance limitations
- **Synology NAS** (DS923+): for file and data storage; also run a few docker containers
- **eero6 router & mesh network**
- **TP-Link un-managed gig switch**
- **APC UPS Pro 1500VA**: for power protection
- **Old HP Laptop**: running Ubuntu server and used for adhoc tasks and testing

Within my home lab, I operate multiple open-source applications, tools, and services. Some of these are deployed within my k3s cluster, and some are deployed using docker/podman or directly on a VM/LXC. I recently migrated several services over from podman to dedicated LXC's using [Proxmox Helper Scripts](https://tteck.github.io/Proxmox/). Here are some other interesting details:

- I employ [traefik](https://traefik.io/) as my reverse proxy for all components, including Kubernetes.
- To access my home lab from anywhere, I rely on [tailscale](https://tailscale.com/) (highly recommended) as my VPN solution.
- I use [k9s](https://k9scli.io/) to help manage my k3s cluster.
- [argocd](https://argoproj.github.io/cd/) serves as my gitops tool within the k3s cluster. Currently, approximately half of my services are deployed using argocd. I am cautious about relying entirely on argocd due to its potential impact on the cluster's performance.
- To handle secrets, I utilize [vault](https://developer.hashicorp.com/vault) and the [argocd-vault-plugin](https://github.com/argoproj-labs/argocd-vault-plugin) to inject secrets into pods as part of my gitops workflow.
- For observability, I employ a combination of tools such as [prometheus](https://prometheus.io/), [grafana](https://grafana.com/), and [loki](https://grafana.com/oss/loki/). I previously used the [kube-prometheus-stack](https://github.com/prometheus-community/helm-charts/tree/main/charts/kube-prometheus-stack) but found it to be too resource intensive for my cluster. Additionally, I rely on [uptime-kuma](https://github.com/louislam/uptime-kuma) to monitor the availability of my public facing services and websites. These are exposed to the internet either using [CloudFlare Pages](https://pages.cloudflare.com/) or [Cloudflare Tunnels](https://developers.cloudflare.com/cloudflare-one/connections/connect-networks/). Finally, I created a simple tool called [python-URLChecker](https://github.com/timmyb824/python-URLChecker) to monitor the availability of internal services. This tool runs within my k3s cluster and sends alerts to my [ntfy](https://ntfy.sh/) server.
- To handle local DNS, I rely on [adguardhome](https://github.com/AdguardTeam/AdGuardHome), and for ad-blocking, I combine adguardhome with [cloudflare](https://www.cloudflare.com/). I've also tried [pi-hole](https://pi-hole.net/) and [technitium](https://technitium.com/dns/), but I found adguardhome to be the simpliest for my needs.

Apart from my home-lab, I have deployed multiple servers within [Oracle Cloud Infrastructure (OCI)](https://www.oracle.com/cloud/) to serve various needs. I use OCI over AWS or GCP because they have a very generous free tier that allows me run multiple servers without incurring any costs. These servers are deployed and manged using [Terraform](https://www.terraform.io/) and [Terraform Cloud](https://app.terraform.io/session).

Here is a screenshot showing some of the applications that are currently deployed in my home-lab:

<img src="homelab_20240812.png"  width="600" height="300">

In the sreenshot above, I am using a tool called [homepage](https://github.com/gethomepage/homepage) to display all of my services in a single page.

If you wish to delve deeper into my home-lab's operations, I have GitHub repositories housing the manifests, docker-compose files, and scripts that facilitate most of my operations. You can locate them here:

- **[docker-apps](https://github.com/timmyb824/docker-apps)**
- **[kubernetes-apps](https://github.com/timmyb824/kubernetes-apps)**
- **[help-scripts](https://github.com/timmyb824/helper-scripts)**

Lastly, I want to mention my dotfiles repository, which contains all of my configuration files for my shell across both macOS and Linux. I used a very powerful tool called [chezmoi](https://www.chezmoi.io/) to manage these files. With chezmoi I am able to encrypt sensitive files, pull secrets from 1password, and use go tempalting to manage more complex configurations. You can find my dotfiles repository here:

- **[dotfiles](https://github.com/timmyb824/dotfiles)**

<h3 align="left">Connect with me:</h3>
<p align="left">
<a href="https://twitter.com/timmyb824" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/twitter.svg" alt="timmyb824" height="30" width="40" /></a>
<a href="https://linkedin.com/in/timothy-bryant-7aa00026" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/linked-in-alt.svg" alt="timothy-bryant-7aa00026" height="30" width="40" /></a>
</p>

<h3 align="left">Stats:</h3>

<p>&nbsp;<img align="center" src="https://github-readme-stats.vercel.app/api?username=timmyb824&show_icons=true&locale=en&theme=tokyonight" alt="timmyb824" /></p>

<img align="center" src="/github-metrics.svg" alt="Metrics" width="400">

<a href="https://app.daily.dev/timmyb824"><img src="https://github.com/timmyb824/timmyb824/blob/main/devcard.png" width="356" alt="Tim Bryant's Dev Card"/></a>

<!-- Old card version:
<a href="https://app.daily.dev/DailyDevTips"><img src="https://github.com/timmyb824/timmyb824/blob/main/devcard.svg" width="400" alt="Tim Bryant's Dev Card"/></a> -->
