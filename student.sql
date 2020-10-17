DROP TABLE IF EXISTS `student`;
CREATE TABLE `student`  (
                            `id` int(11) NOT NULL AUTO_INCREMENT,
                            `age` int(11) DEFAULT NULL,
                            `birth` date DEFAULT NULL,
                            `gender` char(1) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
                            `name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL,
                            `parent` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL,
                            PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_ci ROW_FORMAT = Dynamic;

INSERT INTO `student` VALUES (1, 22, '1998-06-24', '1', 'Andrew', 'Sony');
INSERT INTO `student` VALUES (2, 21, '1999-01-24', '0', 'Tom', 'Jackie');
INSERT INTO `student` VALUES (3, 20, '1920-11-24', '1', 'Johnson', 'Mickey');
