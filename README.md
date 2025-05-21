# 📦 sftpawslambda

Este projeto utiliza a biblioteca `pysftp` em uma AWS Lambda Function. Como `pysftp` não está incluída por padrão no ambiente de execução da Lambda, é necessário criar uma **Lambda Layer** personalizada.

---

## ⚙️ Requisitos

- AWS CLI configurado
- AWS Cloud9 com instância EC2 (Amazon Linux 2)
- Python 3.8
- Permissões IAM para `lambda:PublishLayerVersion`

---

## 🛠️ Passo a Passo

### 1. Criar ambiente EC2 no AWS Cloud9

Acesse o console do **AWS Cloud9** e crie um ambiente baseado em **Amazon Linux 2**.

📚 [Guia oficial AWS – Criando um ambiente EC2 no Cloud9](https://docs.aws.amazon.com/cloud9/latest/user-guide/ec2-environments.html)

---

### 2. Criar política IAM

Crie uma política com permissões para publicar uma Lambda Layer:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AllowLayerPublish",
      "Effect": "Allow",
      "Action": "lambda:PublishLayerVersion",
      "Resource": "*"
    }
  ]
}
```

---

### 3. Criar e associar papel IAM

- Crie uma **IAM Role**
- Anexe a política criada
- Associe a role à instância EC2 do Cloud9

🔐 Agora sua instância poderá publicar Lambda Layers.

---

### 4. Instalar Python 3.8 e pip

```bash
sudo amazon-linux-extras install python3.8 -y
curl -O https://bootstrap.pypa.io/get-pip.py
python3.8 get-pip.py --user
```

---

### 5. Criar pasta e instalar dependências

Substitua `pandas` pelo nome da biblioteca que deseja empacotar (ex: `pysftp`).

```bash
mkdir python
python3.8 -m pip install pysftp -t python/
```

---

### 6. Criar o arquivo zip da Layer

```bash
zip -r layer.zip python
```

---

### 7. Publicar a Layer na AWS

Substitua `us-east-1` pela região da sua função Lambda.

```bash
aws lambda publish-layer-version   --layer-name pysftp-layer   --zip-file fileb://layer.zip   --compatible-runtimes python3.8   --region us-east-1
```

---

### 8. Adicionar a Layer à sua Lambda

No console do AWS Lambda, adicione a layer publicada à sua função.

✅ Pronto! Sua Lambda já pode usar `import pysftp` sem erro.
