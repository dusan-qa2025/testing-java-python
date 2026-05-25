package org.example;

public class FileUploadValidator {
    public static final int MAX_SIZE_MB = 5;

    public boolean isValid(String fileName, Integer fileSize) {
        if (fileName == null || fileName.isEmpty()) {
            return false;
        }

        if (fileSize > MAX_SIZE_MB) {
            return false;
        }

        return hasAllowedExtension(fileName);
    }

    public boolean hasAllowedExtension(String fileName) {
        return fileName.endsWith(".pdf") ||
                fileName.endsWith(".png") ||
                fileName.endsWith(".jpg");
    }
}
