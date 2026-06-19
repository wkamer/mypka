# Raspberry Pi - n8n

[https://www.youtube.com/watch?v=orUY9aRD5Tw](https://www.youtube.com/watch?v=orUY9aRD5Tw)

Install  → Raspberry Pi OS Lite (64-bit)

## Post OS Install

```plain
sudo apt update
```

```plain
sudo apt full-upgrade
```

## Install Docker

```plain
curl -sSL https://get.docker.com | sh
```

## Add user to the Docker Group

```plain
sudo usermod -aG docker $USER
```

## Install Docker Compose

```plain
sudo apt install docker-compose -y
```

## Create a project folder

```plain
mkdir ~/n8n && cd ~/n8n
```

## Clear docker data

```plain
rm -f .env && sudo rm -rf n8n_data && mkdir -p n8n_data && sudo chown -R 1000:1000 n8n_data

```