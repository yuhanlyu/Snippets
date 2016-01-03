A = ' !"#$%&\'()*+,-./0123456789:<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
File.open(ARGV[0]).each_line do |line|
    key, cipher = line.chomp.split(";")
    key = key.each_char.map(&:to_i)
    puts cipher.each_char.with_index
               .map {|c, i| A[(A.index(c) - key[i % key.size]) % A.size]}.join
end
