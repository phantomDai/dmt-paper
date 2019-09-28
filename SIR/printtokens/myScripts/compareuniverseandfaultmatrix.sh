# 这个脚本是为了比较fault-matrix文件与universe文件的测试用例次序是否一致

for((i=1;i<=4130;i++));
do
	content1=`sed -n ${i}p ./fault-matrix`
	content2=`sed -n ${i}p ./universe`
	if [ "$content1" != "$content2" ];then
	       echo $content1 + ${i}
    fi
done	
