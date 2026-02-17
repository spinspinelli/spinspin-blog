# spinspin Blog Icons

Exportierte Icons aus dem spinspin Blog Design.

## 📦 Verfügbare Icons

### 1. Logo Dot (`logo-dot`)
Der charakteristische blaue Punkt aus dem spinspin Logo.
- **Farbe:** #00C2FF (TE Blue)
- **Form:** Kreis
- **Verwendung:** Logo-Akzent, Dekorationselement

### 2. Synth Knob Active (`synth-knob`) ⭐
Das bunte Icon aus der Navigation - Synthesizer-Knopf im aktiven Zustand.
- **Design:** Vertikaler Farbverlauf von Royal Blue (#4169E1) oben zu Lila-Rosa (#B695C0) unten
- **Ring:** Kräftiger blauer Außenring (#4169E1)
- **Markierung:** Weiße vertikale Linie, die über den oberen Rand hinausragt
- **Style:** Retro-Synthesizer-Knopf mit inneren Schatten für 3D-Tiefe
- **Verwendung:** Aktive Navigation, Highlight-Element

### 3. Synth Knob Inactive (`synth-knob-inactive`)
Navigation-Button im inaktiven/Standard-Zustand.
- **Farbe:** #d1d5db (Hell-Grau)
- **Border:** Dunkler Ring (#1a1a1a)
- **Markierung:** Schwarze Linie
- **Style:** Synthesizer-Knopf mit Schatten
- **Verwendung:** Inaktive Navigation, Standard-Zustand

## 📁 Dateistruktur

```
images/
├── logo-dot.svg              # Logo Dot als SVG
├── synth-knob.svg            # Synth Knob Active als SVG
├── synth-knob-inactive.svg   # Synth Knob Inactive als SVG
└── (PNG-Versionen nach Export)
```

## 🎨 PNG Export

### Option 1: HTML Converter (Empfohlen)
1. Öffne `icon-converter.html` im Browser
2. Klicke auf die gewünschte Größe für den Download
3. Oder nutze "Alle Größen herunterladen" für alle Icons

### Option 2: Python Script
**Voraussetzung:** Cairo muss installiert sein
```bash
# macOS mit Homebrew
brew install cairo

# Python-Dependencies
pip install cairosvg

# Script ausführen
python convert_icons.py
```

### Verfügbare Größen
- 64x64px
- 128x128px
- 256x256px
- 512x512px

## 🔧 Verwendung

### Im HTML
```html
<!-- SVG (skalierbar, empfohlen) -->
<img src="images/logo-dot.svg" alt="spinspin">

<!-- PNG (für spezifische Größe) -->
<img src="images/logo-dot-128.png" alt="spinspin" width="128" height="128">
```

### Im CSS
```css
/* Als Background Image */
.logo::after {
    content: '';
    background-image: url('images/logo-dot.svg');
    background-size: contain;
    width: 20px;
    height: 20px;
}
```

### In Markdown
```markdown
![spinspin Logo](images/logo-dot.svg)
```

## 🎨 Design-System

Diese Icons folgen dem spinspin Design-System:
- **Farben:** Teenage Engineering inspirierte Palette
  - TE Blue: #00C2FF
  - TE Pink: #FF006E
  - TE Gray: #d1d5db
- **Stil:** Retro-Tech, Y2K Ästhetik
- **Verwendung:** Konsistent mit dem Blog-Design

## 📝 Lizenz

Diese Icons sind Teil des spinspin Blogs von Spinelli.
Für Verwendung außerhalb des Projekts bitte Kontakt aufnehmen.

## 🔄 Updates

Bei Änderungen am Design:
1. SVG-Dateien in `images/` aktualisieren
2. PNG-Export erneut durchführen
3. Diese README bei neuen Icons ergänzen

---

Erstellt am: 17. Februar 2026
Letzte Aktualisierung: 17. Februar 2026
