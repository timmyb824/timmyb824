<h1 align="left">Hi 👋, I'm Tim Bryant</h1>
<h3 align="left">Passionate about Observability, Site Reliability, DevOps, and Automation</h3>

![Profile views](https://komarev.com/ghpvc/?username=timmyb824&label=Profile%20views&color=0e75b6&style=flat)

- 🌱 Check out my pins for projects I am currently working on or actively commit to

- 🌐 Personal website [🖥️ Official](https://timothybryantjr.com)

- ⚡ Hobbies **Learning new things, breaking and fixing things in my home-lab, axe throwing, pocket knife collecting, 3D printing, pc gaming, watching sports, spending time with my family (Wife, Son, Dog, and Cat)**

<h3 align="left">Homelab:</h3>

I run a small yet capable home-lab within my house, where I constantly experiment to learn new things. Here's a list of the equipment I currently have in my home-lab:

- **Dell Optiplex 5000 PC**
- **Three Beelink Mini PCs**
- **Synology NAS** (DS923+)
- **eero6 router & mesh network**
- **TP-Link un-managed gig switch**
- **APC UPS Pro 1500VA**
- **Old HP Laptop**

Within my home-lab, I run many open-source applications, tools, and services. Many of these are deployed within my k3s cluster, and some are deployed using podman or directly on a VM/LXC. I recently migrated several services over to dedicated LXC's using [Proxmox Helper Scripts](https://tteck.github.io/Proxmox/). Here are some other interesting details:

- I employ [traefik](https://traefik.io/) as my reverse proxy for all components, including Kubernetes.
- I use [authentik](https://www.authentik.io/) for authentication and authorization.
- To access my home lab from anywhere, I rely on [tailscale](https://tailscale.com/) as my VPN solution.
- I use [k9s](https://k9scli.io/) to help manage my k8s cluster.
- [argocd](https://argoproj.github.io/cd/) serves as my gitops tool within the k3s cluster.
- I developed a custom deploy agent script to manage podman deployments through gitops. This script is available [here](https://github.com/timmyb824/homelab-podman-apps/blob/main/deploy/deploy-agent.sh).
- To handle secrets in my k8s cluster, I utilize [vault](https://developer.hashicorp.com/vault) and the [argocd-vault-plugin](https://github.com/argoproj-labs/argocd-vault-plugin) to inject secrets as part of my gitops workflow.
- To handle secrets in my podman deployments, I utilize [sops](https://github.com/getsops/sops) and [age](https://age-encryption.org/).
- For observability, I employ a combination of tools such as [prometheus](https://prometheus.io/), [grafana](https://grafana.com/), and [loki](https://grafana.com/oss/loki/). I previously used the [kube-prometheus-stack](https://github.com/prometheus-community/helm-charts/tree/main/charts/kube-prometheus-stack) but found it to be too resource intensive for my cluster. Additionally, I rely on [uptime-kuma](https://github.com/louislam/uptime-kuma) to monitor the availability of my public facing services and websites. These are exposed to the internet either using [CloudFlare Pages](https://pages.cloudflare.com/) or [Cloudflare Tunnels](https://developers.cloudflare.com/cloudflare-one/connections/connect-networks/). Finally, I created a simple tool called [PingPulse](https://github.com/timmyb824/PingPulse) to monitor the availability of internal services and emit prometheus metrics I alert on. To ensure visibility into critical services such as my three proxmox nodes, I run Zabbix on an Oracle Cloud Infrastructure (OCI) instance.
- To handle local DNS and ad-blocking, I rely on [adguardhome](https://github.com/AdguardTeam/AdGuardHome). I use [cloudflare](https://www.cloudflare.com/) as my DNS provider. I've also tried [pi-hole](https://pi-hole.net/) and [technitium](https://technitium.com/dns/), but I found adguardhome to be the simpliest for my needs.
- I use [renovate](https://github.com/renovatebot/renovate) to keep my dependencies and images up-to-date.

Apart from my home-lab, I have deployed multiple servers within [Oracle Cloud Infrastructure (OCI)](https://www.oracle.com/cloud/) to serve various needs. I use OCI over AWS or GCP because they have a very generous free tier that allows me run multiple servers without incurring any costs. These servers are deployed and manged using [Terraform](https://www.terraform.io/) and [Terraform Cloud](https://app.terraform.io/session).

Here is a screenshot showing some of the applications that are currently deployed in my home-lab:

<img src="homelab_20251125_1.png"  width="750" height="750">
<img src="homelab_20251125_2.png"  width="750" height="750">

In the sreenshot above, I am using a tool called [homepage](https://github.com/gethomepage/homepage) to display all of my services in a single page.

If you wish to delve deeper into my home-lab's operations, I have GitHub repositories housing the manifests, docker-compose files, and scripts that facilitate most of my operations. You can locate them here:

- **[homelab-podman-apps](https://github.com/timmyb824/homelab-podman-apps)**
- **[homelab-k8s-apps](https://github.com/timmyb824/kubernetes-apps)**
- **[homelab-scripts](https://github.com/timmyb824/helper-scripts)**
- **[homelab-ansible](https://github.com/timmyb824/automation_ansible)**
- **[homelab-tool-dns-tracer](https://github.com/timmyb824/homelab-tool-dns-tracer)**

Lastly, I want to mention my **[dotfiles](https://github.com/timmyb824/dotfiles)** repository, which contains all of my configuration files for my shell across both macOS and Linux. I used a very powerful tool called [chezmoi](https://www.chezmoi.io/) to manage these files. With chezmoi I am able to encrypt sensitive files, pull secrets from 1password, and use go tempalting to manage more complex configurations.

<h3 align="left">Connect with me:</h3>
<p align="left">
<a href="https://twitter.com/timmyb824" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/twitter.svg" alt="timmyb824" height="30" width="40" /></a>
<a href="https://linkedin.com/in/timmyb824" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/linked-in-alt.svg" alt="timmyb824" height="30" width="40" /></a>
</p>

<h3 align="left">Stats:</h3>

<!-- <p>&nbsp;<img align="center" src="https://github-readme-stats.vercel.app/api?username=timmyb824&show_icons=true&locale=en&theme=tokyonight" alt="timmyb824" /></p> -->

<p align="left">
  <img width="48%" src="https://github-readme-stats.vercel.app/api?username=timmyb824&show_icons=true&locale=en&theme=tokyonight&line_height=23" alt="timmyb824" /></p>
  <img width="48%" src="https://streak-stats.demolab.com/?user=timmyb824&theme=tokyonight&hide_border=false&date_format=M+j%5B%2C+Y%5D&mode=daily&hide_total_contributions=false&hide_current_streak=false&hide_longest_streak=false&card_height=200" alt="GitHub streak Card" />
</p>

<img align="center" src="/github-metrics.svg" alt="Metrics" width="400">

<a href="https://app.daily.dev/timmyb824"><img src="https://github.com/timmyb824/timmyb824/blob/main/devcard.png" width="356" alt="Tim Bryant's Dev Card"/></a>

<!-- Old card version:
<a href="https://app.daily.dev/DailyDevTips"><img src="https://github.com/timmyb824/timmyb824/blob/main/devcard.svg" width="400" alt="Tim Bryant's Dev Card"/></a> -->
