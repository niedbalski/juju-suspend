Juju suspend/resume
===================

Juju pluging for suspend and resume a juju environment for avoid wasted resources.


# Warning

On development, still not well tested. 

Providers supported: Local (lxc) and OpenStack (nova) .. interested? please add your own to: juju_suspend/providers/

# How it works


ubuntu@niedbalski-xxx:~$ pip install juju-suspend

ubuntu@niedbalski-xxx:~$ juju suspend --novarc=~/novarc --suspend

Suspending machine: fd7cbbfb-2a2d-499a-88bb-1fefd2e0adfc
Suspending machine: e6690b82-18cd-4782-a1dd-f0b4024b2894
Suspending machine: 1977804a-bb3b-4ef8-9bc4-89d81aaffbfb
Suspending machine: 34a84373-5871-48f2-b79f-5f191a06db3b
Suspending machine: deb8193e-0913-4e1e-8d38-2b01a427bacc
Suspending machine: 86bb651e-690b-47ba-87cc-aae542627dcd
Suspending machine: 286cb0bf-d3df-49b3-a9a5-4dfdb71d4a38
Suspending machine: 9b1894ec-daca-4ba6-8023-aec58baf91d5
Suspending machine: ef28c436-3207-47f9-b750-a1d7da9e9527
Suspending machine: 0e994eac-5e73-4937-a044-84047bd1a36c
Suspending machine: 0395cfb0-dcf2-4a0a-bc0e-71903c38cd96
Suspending machine: 35e244ba-8ef4-41b6-903b-802d267781f4
Suspending machine: ec9ecfb6-9fab-4895-b1e5-6896ae960e1c
Suspending machine: 86d5d886-18fb-4150-9c52-6fed3a82e6e2
Suspending machine: 695e36f6-0e48-48bc-9c27-ebe7ef7ff172
Suspending machine: 5fa67990-39a2-4138-8517-0bd78d41f819
Suspending machine: 4a2f67a9-cdee-488e-a3cc-240f9d87c971

ubuntu@niedbalski-xxx:~$ nova list
```
+--------------------------------------+----------------------------+---------+------------+-------------+---------------------------------------------+
| ID                                   | Name                       | Status  | Task State | Power State | Networks                                    |
+--------------------------------------+----------------------------+---------+------------+-------------+---------------------------------------------+
| 17084b53-30a9-4426-91a9-3267816bd40c | juju-niedbalski-machine-0  | ACTIVE  | -          | Running     | niedbalski_admin_net=10.5.0.8               |
| e6690b82-18cd-4782-a1dd-f0b4024b2894 | juju-niedbalski-machine-10 | SHUTOFF | -          | Shutdown    | niedbalski_admin_net=10.5.0.17              |
| fd7cbbfb-2a2d-499a-88bb-1fefd2e0adfc | juju-niedbalski-machine-11 | SHUTOFF | -          | Shutdown    | niedbalski_admin_net=10.5.0.18              |
| 34a84373-5871-48f2-b79f-5f191a06db3b | juju-niedbalski-machine-12 | SHUTOFF | -          | Shutdown    | niedbalski_admin_net=10.5.0.20              |
| 1977804a-bb3b-4ef8-9bc4-89d81aaffbfb | juju-niedbalski-machine-13 | SHUTOFF | -          | Shutdown    | niedbalski_admin_net=10.5.0.21              |
| 86bb651e-690b-47ba-87cc-aae542627dcd | juju-niedbalski-machine-14 | SHUTOFF | -          | Shutdown    | niedbalski_admin_net=10.5.0.22              |
| deb8193e-0913-4e1e-8d38-2b01a427bacc | juju-niedbalski-machine-15 | SHUTOFF | -          | Shutdown    | niedbalski_admin_net=10.5.0.23              |
| 9b1894ec-daca-4ba6-8023-aec58baf91d5 | juju-niedbalski-machine-16 | SHUTOFF | -          | Shutdown    | niedbalski_admin_net=10.5.0.24              |
| 286cb0bf-d3df-49b3-a9a5-4dfdb71d4a38 | juju-niedbalski-machine-17 | SHUTOFF | -          | Shutdown    | niedbalski_admin_net=10.5.0.25              |
| 0e994eac-5e73-4937-a044-84047bd1a36c | juju-niedbalski-machine-18 | SHUTOFF | -          | Shutdown    | niedbalski_admin_net=10.5.0.26              |
| ef28c436-3207-47f9-b750-a1d7da9e9527 | juju-niedbalski-machine-19 | SHUTOFF | -          | Shutdown    | niedbalski_admin_net=10.5.0.27              |
| 5fa67990-39a2-4138-8517-0bd78d41f819 | juju-niedbalski-machine-20 | SHUTOFF | -          | Shutdown    | niedbalski_admin_net=10.5.0.28              |
| 0395cfb0-dcf2-4a0a-bc0e-71903c38cd96 | juju-niedbalski-machine-5  | SHUTOFF | -          | Shutdown    | niedbalski_admin_net=10.5.0.13              |
| 86d5d886-18fb-4150-9c52-6fed3a82e6e2 | juju-niedbalski-machine-6  | SHUTOFF | -          | Shutdown    | niedbalski_admin_net=10.5.0.14              |
| ec9ecfb6-9fab-4895-b1e5-6896ae960e1c | juju-niedbalski-machine-7  | SHUTOFF | -          | Shutdown    | niedbalski_admin_net=10.5.0.15              |
| 4a2f67a9-cdee-488e-a3cc-240f9d87c971 | juju-niedbalski-machine-8  | SHUTOFF | -          | Shutdown    | niedbalski_admin_net=10.5.0.16              |
| 695e36f6-0e48-48bc-9c27-ebe7ef7ff172 | juju-niedbalski-machine-9  | SHUTOFF | -          | Shutdown    | niedbalski_admin_net=10.5.0.19              |
| e9d5b063-1ade-4760-ab2c-0b6f2058e711 | niedbalski-xxx         | ACTIVE  | -          | Running     | niedbalski_admin_net=10.5.0.3, 10.230.18.13 |
+--------------------------------------+----------------------------+---------+------------+-------------+---------------------------------------------+
```
ubuntu@niedbalski-xxx:~$ juju resume --novarc=~/novarc --resume

Resuming machine: fd7cbbfb-2a2d-499a-88bb-1fefd2e0adfc
Resuming machine: e6690b82-18cd-4782-a1dd-f0b4024b2894
Resuming machine: 1977804a-bb3b-4ef8-9bc4-89d81aaffbfb
Resuming machine: 34a84373-5871-48f2-b79f-5f191a06db3b
Resuming machine: deb8193e-0913-4e1e-8d38-2b01a427bacc
Resuming machine: 86bb651e-690b-47ba-87cc-aae542627dcd
Resuming machine: 286cb0bf-d3df-49b3-a9a5-4dfdb71d4a38
Resuming machine: 9b1894ec-daca-4ba6-8023-aec58baf91d5
Resuming machine: ef28c436-3207-47f9-b750-a1d7da9e9527
Resuming machine: 0e994eac-5e73-4937-a044-84047bd1a36c
Resuming machine: 0395cfb0-dcf2-4a0a-bc0e-71903c38cd96
Resuming machine: 35e244ba-8ef4-41b6-903b-802d267781f4
Resuming machine: ec9ecfb6-9fab-4895-b1e5-6896ae960e1c
Resuming machine: 86d5d886-18fb-4150-9c52-6fed3a82e6e2
Resuming machine: 695e36f6-0e48-48bc-9c27-ebe7ef7ff172
Resuming machine: 5fa67990-39a2-4138-8517-0bd78d41f819
Resuming machine: 4a2f67a9-cdee-488e-a3cc-240f9d87c971

ubuntu@niedbalski-xxx:~$ nova list
```
+--------------------------------------+----------------------------+--------+------------+-------------+---------------------------------------------+
| ID                                   | Name                       | Status | Task State | Power State | Networks                                    |
+--------------------------------------+----------------------------+--------+------------+-------------+---------------------------------------------+
| 17084b53-30a9-4426-91a9-3267816bd40c | juju-niedbalski-machine-0  | ACTIVE | -          | Running     | niedbalski_admin_net=10.5.0.8               |
| e6690b82-18cd-4782-a1dd-f0b4024b2894 | juju-niedbalski-machine-10 | ACTIVE | -          | Running     | niedbalski_admin_net=10.5.0.17              |
| fd7cbbfb-2a2d-499a-88bb-1fefd2e0adfc | juju-niedbalski-machine-11 | ACTIVE | -          | Running     | niedbalski_admin_net=10.5.0.18              |
| 34a84373-5871-48f2-b79f-5f191a06db3b | juju-niedbalski-machine-12 | ACTIVE | -          | Running     | niedbalski_admin_net=10.5.0.20              |
| 1977804a-bb3b-4ef8-9bc4-89d81aaffbfb | juju-niedbalski-machine-13 | ACTIVE | -          | Running     | niedbalski_admin_net=10.5.0.21              |
| 86bb651e-690b-47ba-87cc-aae542627dcd | juju-niedbalski-machine-14 | ACTIVE | -          | Running     | niedbalski_admin_net=10.5.0.22              |
| deb8193e-0913-4e1e-8d38-2b01a427bacc | juju-niedbalski-machine-15 | ACTIVE | -          | Running     | niedbalski_admin_net=10.5.0.23              |
| 9b1894ec-daca-4ba6-8023-aec58baf91d5 | juju-niedbalski-machine-16 | ACTIVE | -          | Running     | niedbalski_admin_net=10.5.0.24              |
| 286cb0bf-d3df-49b3-a9a5-4dfdb71d4a38 | juju-niedbalski-machine-17 | ACTIVE | -          | Running     | niedbalski_admin_net=10.5.0.25              |
| 0e994eac-5e73-4937-a044-84047bd1a36c | juju-niedbalski-machine-18 | ACTIVE | -          | Running     | niedbalski_admin_net=10.5.0.26              |
| ef28c436-3207-47f9-b750-a1d7da9e9527 | juju-niedbalski-machine-19 | ACTIVE | -          | Running     | niedbalski_admin_net=10.5.0.27              |
| 5fa67990-39a2-4138-8517-0bd78d41f819 | juju-niedbalski-machine-20 | ACTIVE | -          | Running     | niedbalski_admin_net=10.5.0.28              |
| 0395cfb0-dcf2-4a0a-bc0e-71903c38cd96 | juju-niedbalski-machine-5  | ACTIVE | -          | Running     | niedbalski_admin_net=10.5.0.13              |
| 86d5d886-18fb-4150-9c52-6fed3a82e6e2 | juju-niedbalski-machine-6  | ACTIVE | -          | Running     | niedbalski_admin_net=10.5.0.14              |
| ec9ecfb6-9fab-4895-b1e5-6896ae960e1c | juju-niedbalski-machine-7  | ACTIVE | -          | Running     | niedbalski_admin_net=10.5.0.15              |
| 4a2f67a9-cdee-488e-a3cc-240f9d87c971 | juju-niedbalski-machine-8  | ACTIVE | -          | Running     | niedbalski_admin_net=10.5.0.16              |
| 695e36f6-0e48-48bc-9c27-ebe7ef7ff172 | juju-niedbalski-machine-9  | ACTIVE | -          | Running     | niedbalski_admin_net=10.5.0.19              |
| e9d5b063-1ade-4760-ab2c-0b6f2058e711 | niedbalski-xxx         | ACTIVE | -          | Running     | niedbalski_admin_net=10.5.0.3, 10.230.18.13 |
+--------------------------------------+----------------------------+--------+------------+-------------+---------------------------------------------+
```
