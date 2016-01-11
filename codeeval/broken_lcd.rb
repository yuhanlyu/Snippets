lcd = ["11111100", "01100000", "11011010", "11110010", "01100110", "10110110", 
       "10111110", "11100000", "11111110", "11110110", "00000001"]
File.open(ARGV[0]).each_line do |line|
    dis, n = line.chomp.split(";")
    dis, n = dis.split, n.split("")
    correct = []
    n.size.times {|i|
        if n[i] == "."
            correct[-1][-1] = "1"
        else
            correct << lcd[n[i].to_i].clone
        end
    }
    puts dis.each_cons(correct.size).map {|s| s.zip(correct)}
            .any?{|p| p.all? {|a,b| a.size.times.all? {|i| 
                b[i] == "0" || a[i] == "1"}}} ? "1" : "0"
end
