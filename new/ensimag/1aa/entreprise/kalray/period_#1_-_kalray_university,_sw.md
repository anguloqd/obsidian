# Period #1 - Kalray University, SW

Date de création: October 30, 2024 10:25 AM
Modifié: November 14, 2024 5:10 PM

[https://kalrayinc.sharepoint.com/sites/KALRAY/Shared%20Documents/Forms/AllItems.aspx?csf=1&web=1&e=5ZxLYN&CID=f8fbb2d1%2D5b66%2D4bfa%2D89cf%2D1c2cf75bd216&FolderCTID=0x01200036A3007A2388314190E8A96E76235C37&id=%2Fsites%2FKALRAY%2FShared%20Documents%2FGeneral%2FKALRAY%20UNIVERSITY%2FLearning%20Material%2FSW&viewid=53d3044c%2Dd08b%2D4c86%2Db2dc%2D1a88300aaf9b](https://kalrayinc.sharepoint.com/sites/KALRAY/Shared%20Documents/Forms/AllItems.aspx?csf=1&web=1&e=5ZxLYN&CID=f8fbb2d1%2D5b66%2D4bfa%2D89cf%2D1c2cf75bd216&FolderCTID=0x01200036A3007A2388314190E8A96E76235C37&id=%2Fsites%2FKALRAY%2FShared%20Documents%2FGeneral%2FKALRAY%20UNIVERSITY%2FLearning%20Material%2FSW&viewid=53d3044c%2Dd08b%2D4c86%2Db2dc%2D1a88300aaf9b)

# FLOSS - SW Licensing

## …

# Getting Started with Kalray Technologies

## SDK introduction

![image.png](period_#1_-_kalray_university,_sw/image.png)

You can use MPPA in direct programming in two ways:

- kvx-jtag-runner: prototyping, evaluating, benchmarking.
- OpenCL: deployment, heterogeneous applications execution.

![image.png](period_#1_-_kalray_university,_sw/image_1.png)

A comprehensive Neural Network offer, from standard CNN frameworks to code generation, setup & multiple CNN execution. A flexible tool, with capability to customize
neural networks and runtime execution.

- Fast execution of pre-trained Neural Network
- Fully optimized tools towards best performance
    - Optimized layers | scheduling | data path
- Similar to vendors-specific inference tools
- Support of major image-based networks
    - Classification | Detection | Segmentation

KANN is OpenCL based and can be run in parallel with other OpenCL application.

## KaNN

![On MPPA processor, each layer is parallelized on all available clusters for a low latency CNN.](period_#1_-_kalray_university,_sw/image_2.png)

On MPPA processor, each layer is parallelized on all available clusters for a low latency CNN.

CNN layers can be viewed as a 3D pixel matrix, very similar to a 2D image with multiple channels.

- Not only 3 as on RGB image but typically between 100 and 1000).
- Pixels were originally 32-bit floating point and can now be anything from floating-point (16 or 32 bits) to integers (from 1 to 32 bits generally)

Similarly, to standard image processing pipeline, during inference each layer is used to produce a new image:

- Convolution, average, sampling, unit linear rectifier (reLU), local response normalization (LRN), softmax, deconvolution, …
- Layers are executed sequentially to form the whole CNN.
- This means, there are dependencies between layers.

But the pipeline have two main drawbacks:

- Increase the latency
- Cause unbalanced loads

## Kalray Product Offer

![image.png](period_#1_-_kalray_university,_sw/image_3.png)

# Tools & methods for software development at Kalray

## Working environments

### OS

Linux is the main (and only) OS for software development in Kalray. For software, the “standard” linux distribution are ubuntu22.04 for CV2 and ubuntu18.04 for CV1 (for now). There is also limited support for redhat8, mainly because HW tools are only available on redhat.

- You are a sudoer for apt commands on your workstation
- If you have a powerful workstation you can work locally and build locally. If it’s not the case there are compute servers and Kalray devices allocated by team.

Linux and Windows workstations are under 2 separate networks. Marketing, training, planning tasks, etc... are mainly performed on windows.

(Note: laptops should use WIFI, or must be plugged on windows network, regardless their OS)

### Filesystems

Your `$HOME` directory is on a NFS (Network File System). The NFS is backed up regularly.

Please do not use the NFS for volatile data such as builds, browser cache, ccache data, etc…Please use `/work1/<login>` for those instead. `/work1` is always mapped to local disk on all Kalray machines, high speed and never backed up.

![image.png](period_#1_-_kalray_university,_sw/image_4.png)

### ❗: Working remotely (SSH mainly)

`.ssh/config`

```bash
Host <your_machine>

    ProxyCommand ssh -T -p 22 -i /home/LOGIN/.ssh/id_xraynaud kalray@ssh.kalray.eu
    # Redirect ports
    DynamicForward *:8090 # Mandatory for browsing internal web, cf proxy.pac next slide
    LocalForward 9999 localhost:22 # Easy ssh access to Kalray after the 1st connection
    # Other examples: VNC, X11, web-services, etc...
    LocalForward 24800 localhost:24800
    LocalForward 8080 localhost:8080
    PubkeyAuthentication no
    ForwardX11 yes

# This second configuration allows opening a single shell without port redirection, and using authentication of the first connection (less passwd)

Host Kalray

    Hostname localhost
    Port 9999
    ForwardX11 yes
    identityfile ~/.ssh/id_rsa
```

For the proxy: [http://data.kalrayinc.com/proxy.pac](http://data.kalrayinc.com/proxy.pac)

```bash
function FindProxyForURL(url, host) {

  if (shExpMatch(url,"https://mail.kalray.eu/*"))     {return "DIRECT";}
  if (isInNet(host, "192.168.38.0", "255.255.255.0")) { return "DIRECT";}
  if (shExpMatch(url,"*cse.kalray.eu/*"))             {return "DIRECT";}
  if (shExpMatch(url,"*.kalray.eu/*"))                {return "SOCKS5 localhost:8090; DIRECT";}
  if (shExpMatch(url, "*.kalray.eu:*/*"))             {return "SOCKS5 localhost:8090; DIRECT";}
  if (shExpMatch(url,"*.lan.kalrayinc.com/*"))        {return "SOCKS5 localhost:8090; DIRECT";}
  if (shExpMatch(url, "*.lan.kalrayinc.com:*/*"))     {return "SOCKS5 localhost:8090; DIRECT";}
  if (isInNet(host, "192.168.0.0",  "255.255.0.0"))   {return "SOCKS5 localhost:8090; DIRECT";}
  if (isInNet(host, "172.16.0.0", "255.255.0.0")) { return "SOCKS5 localhost:8090; DIRECT";}
  return "DIRECT";
}
```

Manipulation that Bjorn did to me: this avoids entering the password like 99 times.

```bash
# in C:\Users\dangulo, local laptop
ssh-keygen -f .ssh/dangulo_win -t ecdsa -b 521
scp .ssh\dangulo_win* dangulo@kalray:.ssh/

# Pseudo-terminal will not be allocated because stdin is not a terminal.
# Enter passphrase for key 'C:\Users\dangulo/.ssh/id_dangulo_remote':
# dangulo@kalray's password:
# dangulo_win                         100%  748    15.5KB/s   00:00
# dangulo_win.pub                     100%  282     5.9KB/s   00:00

ssh ws2405

# Enter passphrase for key 'C:\Users\dangulo/.ssh/id_dangulo_remote':
# dangulo@kalray's password:
# Enter passphrase for key 'C:\Users\dangulo/.ssh/id_dangulo_remote':
# dangulo@192.168.37.180's password:
```

Once that is done, modify both (host and workstation) `~/.ssh/config` such that:

```bash
# In workstation, then ~/.ssh/config

host git
...

host gerrit
...

Host ws2405
  HostName 192.168.37.180
  User dangulo
  IdentityFile ~/.ssh/dangulo_win
  ProxyJump dangulo@kalray
  LocalForward 8888 localhost:8888
  LocalForward 8889 localhost:8889
  LocalForward 8080 localhost:8080
  LocalForward 6000 localhost:6000
  ForwardX11 yes

Host kalray
  ProxyCommand ssh -i ~/.ssh/id_dangulo_remote kalray@ssh.kalray.eu
  DynamicForward *:8090
  # Redirect remote ports to local ports
  LocalForward 4444 localhost:22
  LocalForward 3389 winapp.kalray.eu:3389
 
# Cool. Then, in local laptop, then ~/.ssh/config

Host ws2405
  HostName 192.168.37.180
  User dangulo
  IdentityFile ~/.ssh/dangulo_win
  ProxyJump dangulo@kalray
  LocalForward 8888 localhost:8888
  LocalForward 8889 localhost:8889
  LocalForward 8080 localhost:8080
  LocalForward 6000 localhost:6000
  ForwardX11 yes

Host kalray
  ProxyCommand ssh -i ~/.ssh/id_dangulo_remote kalray@ssh.kalray.eu
  DynamicForward *:8090
  # Redirect remote ports to local ports
  LocalForward 4444 localhost:22
  LocalForward 3389 winapp.kalray.eu:3389
```

Then, other modifications Bjorn told me such that I can access `kalray` (`Jade` in my case) from VSCode, and also `jetson01` from VSCode:

```bash
# WINDOWS .ssh/config FILE
#LogLevel DEBUG3

Host ws2405
  HostName 192.168.37.180
  User dangulo
  IdentityFile ~/.ssh/dangulo_win
  ProxyJump dangulo@kalray
  LocalForward 8888 localhost:8888
  LocalForward 8889 localhost:8889
  LocalForward 8080 localhost:8080
  LocalForward 6000 localhost:6000
  ForwardX11 yes

Host kalray
  ProxyCommand ssh -i ~/.ssh/id_dangulo_remote kalray@ssh.kalray.eu
  # Remove this, for some reason it doesn't work
  # IdentityFile ~/.ssh/id_dangulo_remote
  User dangulo
  DynamicForward *:8090
  # Redirect remote ports to local ports
  LocalForward 4444 localhost:22
  LocalForward 3389 winapp.kalray.eu:3389

Host jetson01
	ProxyJump kalray # needs to pass through kalray (jade in my case)
  HostName 192.168.39.2
  ForwardX11 yes
  User accesscore
	IdentityFile ~/.ssh/dangulo_win
```

<aside>
❓

```bash
# At a given moment I executed this,
# I think it was to automate
# the login process, but I'm not sure

ssh-copy-id -i .ssh/dangulo_win dangulo@ws2405
```

</aside>

Then, to automatize `jetson01` login (from `ws2405`, for some reason. maybe works from somewhere else): this takes your password to access jetson01 and crypts it then stores it in the file `.ssh/authorized_keys`.

```bash
dangulo@ws2405:~/.ssh$ ssh-copy-id -i ~/.ssh/dangulo_win jetson01

# /usr/bin/ssh-copy-id: INFO: Source of key(s) to be installed: "/nfs/home/dangulo/.ssh/dangulo_win.pub"
# /usr/bin/ssh-copy-id: INFO: attempting to log in with the new key(s), to filter out any that are already installed
# /usr/bin/ssh-copy-id: INFO: 1 key(s) remain to be installed -- if you are prompted now it is to install the new keys
# accesscore@192.168.39.2's password: ### YOU WRITE THE PASSWORD HERE, THEN IT GETS CRYPTED AND STORED ##
#
# Number of key(s) added: 1
#
# Now try logging into the machine, with:   "ssh 'jetson01'"
# and check to make sure that only the key(s) you wanted were added.
```

## System architecture

![image.png](period_#1_-_kalray_university,_sw/image_5.png)

## Kalray Projects (ACB, ACS, ACE)

![image.png](period_#1_-_kalray_university,_sw/image_6.png)

## GIT & Gerrit

### Gerrit

All projects in Kalray are managed by **gerrit**.

Run `ssh gerrit gerrit ls-projects` gives all git repos.

Some hooks are present for all gits, in order to:​

- Launch Jenkins jobs​
- Avoid committing huge files​
- Detecting whether a submodule has not been pushed​
- Updating Jira Tickets​
- Launch linters…

Warning: Jenkins controls the code review (and not the contrary).

```bash
# Setup
$ Export PATH=$PATH:/nfs/tools/software/kerrit
$ installCommitHook # need to run this command only once on your gits repos
```

```bash
# Commit & Code Review
$ git commit
$ kerrit [--reviewer login …] 
# got to gerrit.kalray.eu
# iterate…
```

### Git branches conventions

Regarding ACB conventions…

- **main** is the main development branch.​
- Release branches are created at the end of each product increment (PI), named `release/X.Y.Z`
- **It’s not possible to push on this branch directly.**

Regarding BU (ACE & ACS) conventions…

- **master** is the main development branch​
- **main** branch is kept, to verify that ACB does not broke anything​
- A release branch is created for each release, at end of PI, named `release/X.Y.Z` (as for ACB)
- **It’s not possible to push on this branch directly.**

The user develops in their own branch. For the next branches, the **red** part of the branch is the target branch (the target branch is created or updated upon successful integration), and the **green** part of the branch is optional (to use at your convenience).

- `aci/<user>.whatever/main`
- `aci/<user>.whatever/dirty.yyyyy`, 	`aci/<user>.whatever/dryrun.yyyyy`
    - `dirty` and `dryrun` branches do not perform any merge and do not propagate.
- `aci/<user>.whatever/XXX.from.main`, `aci/<user>.whatever/XXX.from.release/4.2.0`
    - Branches matching "`*.from.*`" are propagated to dependent projects in integration.
    - **If the branch does not exist, it creates it automatically from** main (or `release/4.6.0`).
- `aci/<user>.whatever/release/4.6.0`
- `<dev|tmp>/<user>.whatever/whatever_you_want`
    - Branches starting with "`dev`" or "`tmp`" instead of "`aci`" **do not trig integration**.

Regarding branch management, a lot of branches are created by integration:

- `tmp/<date>`: such branches are deleted after 1 week
- `user/.*\.hudson- branches`:  such branches are deleted after 3 month

Your branches may be deleted as well:

- `user/*` and `aci/*` branches are deleted after 3 month, only if they have been merged in "`master`“, “`main`” or "`coolidge`"
- `*.from.*` branches are deleted after 6 month

A good practice is to run `git remote update --prune` from time to time.
Note: scripts on charge of this deletion are in SigmaCToolchainScripts: remove*branches-rec

## Good practices

### Commit conventions

Commit title on the first line (line 1). It should be short and describe what the commit does (How ?). If the project contains many components, you can put the component name followed by a column at the beginning of the line.

Then, an empty line must be present (line 2).

After that, the commit message can be described, starting at line 3. It should describe **what** has been done, and **why**. Keep lines short whenever you can (80 char per line is the rule of thumb)

Finally, references to tickets/revisions should be placed at the end of the commit.

Example here:

```
core: Add support for feature xxxx

This commit adds support for features xxx using xxxx. To do so,
the core framework has been rework by adding a new function. This
new function has been added to allow handling the new feature but
without breaking the legacy functionality.

Ref TICKET-XXXX
```

## Metabuild and Build.rb

…

## **Git repos, rev_files and KalrayEnvs**

## **Jenkins**

## **Toolchain Documentation**

Toolchain documentation is available at [https://docs.kalray.eu](https://docs.kalray.eu/) (internal web site).

Public docs in the toolchain must be available in RST/sphinx format.​

(There are still some docs in LaTeX and a few in .PPT)

When creating docs, please contact Kevin Quintin for further info.