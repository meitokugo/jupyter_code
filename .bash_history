git config --global mingdebaba
git config --global mingdebaba
git config --global user.name mingdebaba
git config --global user.email 694104133@qq.com
git config --global push.default matching
git config --global core.quotepath false
git config --global core.editor "vim"
$ ssh-keygen -t ed25519 -C "694104133@qq.com"
ssh-keygen -t ed25519 -C "694104133@qq.com"
at ~/.ssh/id_rsa.pub
cat ~/.ssh/id_rsa.pub
cat ~/.ssh/id_rsa.pub
ssh-keygen -t ed25519 -C "694104133@qq.com"
ssh-keygen -t ed25519 -C "694104133@qq.com"
cat ~/.ssh/id_rsa.pub
ssh-keygen -t rsa -b 4096 -C "694104133@qq.com"
Generating public/private ed25519 key pair.
> Generating public/private ed25519 key pair.
cat ~/.ssh/id_rsa.pub
echo "# blabla" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin git@github.com:mingdebaba/blabla.git
