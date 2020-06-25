# Editing .sh files in VS Code on Windows

In case you are editing .sh files in Windows, you might encounter error at runtime in  WSL because of the default CRLF line ending applied. 
You can fix existing files with command `sed -i.bak 's/\r$//' azure-deploy.sh` [see this discussion](https://askubuntu.com/questions/803162/how-to-change-windows-line-ending-to-unix-version) and if you are using VS Code you can [configure line ending](https://github.com/Microsoft/vscode/issues/2957)