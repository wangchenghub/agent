#!/bin/bash

version=$1

if [[ -z $version ]];then
  echo -e "\033[31m--------没有定义版本号！--------\033[0m"
  exit 1
fi

ver=$2

if [[ $2 == "debug" ]];then
  ver="debug"
elif [[ $2 == "test" ]];then
  ver="test"
else
  ver="build"
fi

sev_name="agent"
base_path=`pwd`
dir_name="$sev_name-$version"
tmp_dir="/tmp/$dir_name"
export_path="$base_path/export"

file_name="$sev_name-$version.tar"

[[ -d $export_path ]] || mkdir -p $export_path


function is_fail(){
    if [[ $1 -ne 0 ]];then
        echo -e "\033[31m--------打包过程出错--------\033[0m"
        echo -e "\033[31m----------打包失败----------\033[0m"
        [[ $1 -eq 1 ]] && exit 1;
    fi
}


function clean(){
    echo -e "\033[36m--------清理临时文件--------\033[0m"
    rm -rf $tmp_dir
    rm -rf $base_path/dist
    rm -rf $base_path/init_agent.egg-info
}

echo -e "\033[35m版本号：\033[0m\033[34m$version\033[0m  \033[35m构建版本：\033[0m\033[34m$ver\033[0m"

echo -e "\033[35m --------打包源代码--------\033[0m"
chmod +x run.sh
python3 setup.py sdist
is_fail $?

echo -e "\033[36m--------开始打包流程--------\033[0m"
[[ -d $tmp_dir ]] && rm -rf $tmp_dir
mkdir -p $tmp_dir

echo -e "\033[36m--------正在构建镜像--------\033[0m"
docker build -t $sev_name:v$version .
is_fail $?

echo -e "\033[36m--------正在导出镜像--------\033[0m"
docker save -o $tmp_dir/$file_name $sev_name:v$version
is_fail $?

echo -e "\033[36m--------正在打包镜像--------\033[0m"
cd /tmp && tar zcf ${file_name}.gz $dir_name && mv ${file_name}.gz $export_path
is_fail $?

clean

echo -e "\033[32m打包完成,文件位置:\033[0m \033[33m$export_path/${file_name}.gz\033[0m"



