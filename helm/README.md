# Helm Chart Setup

This project includes custom Helm Charts for both:

* MySQL
* Flask Secret Santa Application

---

## Folder Structure

```text
helm/
│
├── mysql-chart/
│
├── flask-secret-santa-app-chart/
│
└── README.md

---

## Create Helm Chart

Create a new Helm chart:

```bash
helm create mysql-chart
```

```bash
helm create flask-secret-santa-app-chart
```

---

## Validate Chart

Check chart syntax and best practices:

```bash
helm lint ./mysql-chart
```

```bash
helm lint ./flask-secret-santa-app-chart
```

---

## Render Templates

Generate Kubernetes manifests without deploying:

```bash
helm template mysql-release ./mysql-chart
```

```bash
helm template flask-release ./flask-secret-santa-app-chart
```

---

## Install MySQL Chart

```bash
helm install mysql-release ./mysql-chart
```

Verify:

```bash
kubectl get all
```

---

## Install Flask Application Chart

```bash
helm install flask-release ./flask-secret-santa-app-chart
```

Verify:

```bash
kubectl get all
```

---

## List Installed Releases

```bash
helm list
```

---

## Check Release Status

```bash
helm status mysql-release
```

```bash
helm status flask-release
```

---

## Upgrade Existing Release

After updating templates or values:

```bash
helm upgrade mysql-release ./mysql-chart
```

```bash
helm upgrade flask-release ./flask-secret-santa-app-chart
```

---

## View Release Values

```bash
helm get values mysql-release
```

```bash
helm get values flask-release
```

---

## Package Helm Chart

Create a distributable Helm package:

```bash
helm package ./mysql-chart
```

```bash
helm package ./flask-secret-santa-app-chart
```

Output:

```text
mysql-chart-0.1.0.tgz
flask-secret-santa-app-chart-0.1.0.tgz
```

---

## Rollback Release

View revision history:

```bash
helm history flask-release
```

Rollback to previous version:

```bash
helm rollback flask-release 1
```

---

## Uninstall Release

Remove Flask application:

```bash
helm uninstall flask-release
```

Remove MySQL:

```bash
helm uninstall mysql-release
```

---

## Useful Helm Commands

```bash
helm version

helm repo list

helm list

helm lint <chart-name>

helm template <release-name> <chart>

helm install <release-name> <chart>

helm upgrade <release-name> <chart>

helm history <release-name>

helm rollback <release-name> <revision>

helm uninstall <release-name>

helm package <chart>
```

