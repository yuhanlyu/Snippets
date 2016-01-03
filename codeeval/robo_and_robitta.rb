require 'scanf'
File.open(ARGV[0]).each_line do |line|
    line.scanf("%dx%d | %d %d") {|m, n, x, y|
        ans = 0
        ans, m, n, x, y = ans + m, n - 1, m, n - y, x while n > y
        puts ans + x
    }
end
