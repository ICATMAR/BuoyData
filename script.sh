#!/bin/bash

# Define el directorio base
DIR="/home/adriamarti/Escritorio/ICM/Tasques/BoiaBCN/BuoyData"
ROOT="$DIR"

# Directorios y archivos
SOMORROSTRO_DIR="$DIR/Somorrostro"
TEMPORAL_MDS_DIR="$DIR/temporal_mds"
LAST_UPDATE_FILE="$SOMORROSTRO_DIR/last_update.txt"

# Mapear carpetas a scripts
declare -A FOLDERS_TO_SCRIPTS=(
    ["$SOMORROSTRO_DIR/Doppler"]="$ROOT/proces_data/data_proces_Doppler.py"
    ["$SOMORROSTRO_DIR/Meteo"]="$ROOT/proces_data/data_proces_Meteo.py"
    ["$SOMORROSTRO_DIR/Sami"]="$ROOT/proces_data/data_proces_Sami.py"
    ["$SOMORROSTRO_DIR/SBE37_SMPO"]="$ROOT/proces_data/data_proces_SBE37_SMPO.py"
    ["$SOMORROSTRO_DIR/System"]="$ROOT/proces_data/data_proces_System.py"
    # Agrega más carpetas y scripts según sea necesario
)

# Mapear archivos a scripts
declare -A FILES_TO_SCRIPTS=(
    ["$TEMPORAL_MDS_DIR/BoiaBarcelona_Doppler.dat"]="$ROOT/proces_data/data_proces_Doppler.py"
    ["$TEMPORAL_MDS_DIR/BoiaBarcelona_Meteo.dat"]="$ROOT/proces_data/data_proces_Meteo.py"
    ["$TEMPORAL_MDS_DIR/BoiaBarcelona_Sami.dat"]="$ROOT/proces_data/data_proces_Sami.py"
    ["$TEMPORAL_MDS_DIR/BoiaBarcelona_SBE37_SMPO.dat"]="$ROOT/proces_data/data_proces_SBE37_SMPO.py"
    ["$TEMPORAL_MDS_DIR/BoiaBarcelona_System.dat"]="$ROOT/proces_data/data_proces_System.py"
    # Agrega más archivos y scripts según sea necesario
)

while true; do
    # Obtiene la última fecha de modificación guardada
    if [ -f "$LAST_UPDATE_FILE" ]; then
        LAST_UPDATE=$(cat "$LAST_UPDATE_FILE")
    else
        echo "0" > "$LAST_UPDATE_FILE"
        LAST_UPDATE=0
    fi
    echo "Última fecha de modificación guardada: $LAST_UPDATE"

    # Revisa si las carpetas están vacías
    for FOLDER in "${!FOLDERS_TO_SCRIPTS[@]}"; do
        if [ -d "$FOLDER" ] && [ -z "$(ls -A "$FOLDER")" ]; then
            echo "Carpeta $FOLDER está vacía. Ejecutando script: ${FOLDERS_TO_SCRIPTS[$FOLDER]}"
            /bin/python3 "${FOLDERS_TO_SCRIPTS[$FOLDER]}"
        else
            echo "Carpeta $FOLDER no está vacía."
        fi
    done

    # Revisa si los archivos han sido actualizados
    for FILE in "${!FILES_TO_SCRIPTS[@]}"; do
        if [ -f "$FILE" ]; then
            FILE_TIME=$(stat -c %Y "$FILE")
            echo "Revisando archivo: $FILE con fecha de modificación: $FILE_TIME"

            # Compara la fecha de modificación del archivo con la última guardada
            if (( FILE_TIME > LAST_UPDATE )); then
                # Actualiza la última fecha de modificación guardada
                echo "$FILE_TIME" > "$LAST_UPDATE_FILE"
                echo "Archivo $FILE actualizado. Ejecutando script: ${FILES_TO_SCRIPTS[$FILE]}"

                # Ejecuta el script correspondiente
                /bin/python3 "${FILES_TO_SCRIPTS[$FILE]}"
            else
                echo "Archivo $FILE no ha sido modificado desde la última comprobación."
            fi
        else
            echo "Archivo $FILE no encontrado."
        fi
    done

    # Espera 5 minutos antes de la siguiente comprobación
    echo "Esperando 5 minutos antes de la siguiente comprobación..."
    sleep 300
done