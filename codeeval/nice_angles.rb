File.open(ARGV[0]).each_line do |line|
    degree = line.to_f
    minutes = (degree - degree.floor) * 60
    seconds = (minutes - minutes.floor) * 60
    printf("%d.%02d'%02d\"\n", degree.floor, minutes.floor, seconds.floor)
end
