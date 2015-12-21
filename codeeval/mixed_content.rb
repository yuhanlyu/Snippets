File.open(ARGV[0]).each_line do |line|
    words, nums = line.chomp.split(",").partition {|x| x.to_i.to_s != x}
                                       .map {|x| x.join(",")}
    puts words + ((words.length > 0 and nums.length > 0) ? "|" : "") + nums
end
