File.open(ARGV[0]).each_line do |line|
    puts line.strip.match(/(?:^[^ @"<>]+|".*")@(?:[A-Z0-9]+?(?:-*[A-Z0-9]+)*\.)+[A-Z]+$/i) ?  "true" : "false"
end
