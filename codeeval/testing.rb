File.open(ARGV[0]).each_line do |line|
    p, t = line.chomp.split(" | ").map(&:each_char)
    case p.zip(t).map {|c, d| c != d}.count(true)
    when 0
        puts "Done"
    when 1..2
        puts "Low"
    when 3..4
        puts "Medium"
    when 5..6
        puts "High"
    else
        puts "Critical"
    end
end
